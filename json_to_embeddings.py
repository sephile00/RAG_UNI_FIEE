import json
import os
import shutil
from tqdm import tqdm
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunking_inteligente(texto, filename):
    """Divide el texto de manera inteligente según el tipo de documento"""
    
    if "calendario" in filename.lower() or "cronograma" in filename.lower():
        # Para calendarios, dividir por fechas/actividades
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50,
            separators=["\n", "FECHA", "ACTIVIDAD", "Del", "Hasta"]
        )
    elif "tramite" in filename.lower() or "guia" in filename.lower():
        # Para guías de trámites, dividir por procedimientos
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n\n", "\n", "Trámites:", "Requisitos:", "•"]
        )
    else:
        # División general
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=80,
            separators=["\n\n", "\n", ". ", " "]
        )
    
    return splitter.split_text(texto)

def limpiar_texto(texto):
    """Limpia y normaliza el texto extraído"""
    import re
    
    # Remover caracteres extraños del OCR
    texto = re.sub(r'[^\w\s\.\,\:\;\(\)\-\n]', ' ', texto)
    
    # Normalizar espacios
    texto = re.sub(r'\s+', ' ', texto)
    
    # Remover líneas muy cortas (probablemente ruido del OCR)
    lineas = texto.split('\n')
    lineas_filtradas = [linea.strip() for linea in lineas if len(linea.strip()) > 10]
    
    return '\n'.join(lineas_filtradas)

def extraer_metadatos_avanzados(item):
    """Extrae metadatos más detallados del contenido"""
    texto = item.get("texto", "").lower()
    filename = item.get("filename", "")
    
    metadatos = {
        "filename": filename,
        "ruta": item.get("ruta"),
        "tipo": item.get("tipo"),
        "temas": []
    }
    
    # Detectar temas principales
    if any(palabra in texto for palabra in ["matricula", "inscripcion", "registro"]):
        metadatos["temas"].append("matricula")
    
    if any(palabra in texto for palabra in ["nota", "calificacion", "reclamo"]):
        metadatos["temas"].append("notas")
        
    if any(palabra in texto for palabra in ["retiro", "abandono"]):
        metadatos["temas"].append("retiro")
        
    if any(palabra in texto for palabra in ["traslado", "cambio"]):
        metadatos["temas"].append("traslado")
        
    if any(palabra in texto for palabra in ["fecha", "cronograma", "calendario"]):
        metadatos["temas"].append("fechas")
        
    if any(palabra in texto for palabra in ["examen", "parcial", "final"]):
        metadatos["temas"].append("examenes")
        
    if any(palabra in texto for palabra in ["pago", "costo", "precio"]):
        metadatos["temas"].append("pagos")
    
    # Detectar año/ciclo si está presente
    import re
    años = re.findall(r'202[0-9]', texto)
    if años:
        metadatos["año"] = años[0]
    
    ciclos = re.findall(r'202[0-9]-[0-9]', texto)
    if ciclos:
        metadatos["ciclo"] = ciclos[0]
    
    return metadatos

def main():
    vector_db_path = "vector_db_imagenes"
    
    # Limpiar base de datos anterior
    if os.path.exists(vector_db_path):
        shutil.rmtree(vector_db_path)
        print("🗑️  Base de datos anterior eliminada.")
    
    # Cargar datos
    try:
        with open("textos_extraidos.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
        print(f"📄 Cargados {len(datos)} documentos")
    except FileNotFoundError:
        print("❌ No se encontró el archivo textos_extraidos.json")
        return
    
    docs = []
    
    # Procesar cada documento
    for item in tqdm(datos, desc="📝 Procesando documentos"):
        texto_original = item.get("texto", "")
        
        if not texto_original.strip():
            continue
            
        # Limpiar texto
        texto_limpio = limpiar_texto(texto_original)
        
        if len(texto_limpio) < 50:  # Skip textos muy cortos
            continue
        
        # Extraer metadatos avanzados
        metadatos = extraer_metadatos_avanzados(item)
        
        # Aplicar chunking inteligente
        chunks = chunking_inteligente(texto_limpio, item.get("filename", ""))
        
        # Crear documentos para cada chunk
        for i, chunk in enumerate(chunks):
            if len(chunk.strip()) > 30:  # Solo chunks significativos
                metadatos_chunk = metadatos.copy()
                metadatos_chunk["chunk_id"] = i
                metadatos_chunk["total_chunks"] = len(chunks)
                
                docs.append(Document(
                    page_content=chunk,
                    metadata=metadatos_chunk
                ))
    
    if not docs:
        print("❌ No se generaron documentos válidos")
        return
    
    print(f"📚 Generados {len(docs)} chunks de documentos")
    
    # Crear embeddings
    print("🧠 Cargando modelo de embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    
    # Crear base de datos FAISS
    print("🔨 Generando embeddings y creando FAISS...")
    db = FAISS.from_documents(docs, embeddings)
    
    # Guardar base de datos
    db.save_local(vector_db_path)
    print(f"✅ {len(docs)} documentos guardados en FAISS exitosamente!")
    
    # Estadísticas
    tipos = {}
    temas = {}
    for doc in docs:
        tipo = doc.metadata.get('tipo', 'desconocido')
        tipos[tipo] = tipos.get(tipo, 0) + 1
        
        for tema in doc.metadata.get('temas', []):
            temas[tema] = temas.get(tema, 0) + 1
    
    print("\n📊 Estadísticas:")
    print("Tipos de documentos:")
    for tipo, cantidad in tipos.items():
        print(f"  - {tipo}: {cantidad} chunks")
    
    print("\nTemas identificados:")
    for tema, cantidad in temas.items():
        print(f"  - {tema}: {cantidad} chunks")

if __name__ == "__main__":
    main()