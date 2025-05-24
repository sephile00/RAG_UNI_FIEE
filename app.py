from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from datetime import datetime
import json

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY no encontrada. Por favor, configura esta variable de entorno.")

class ChatbotNatural:
    def __init__(self):
        self.llm_clasificador = ChatOpenAI(
            model_name="gpt-4o-mini",
            temperature=0.1,
            max_tokens=50
        )
        
        self.llm_conversacional = ChatOpenAI(
            model_name="gpt-4o-mini",
            temperature=0.8,
            max_tokens=800
        )
        
        self.llm_tecnico = ChatOpenAI(
            model_name="gpt-4o-mini",
            temperature=0.3,
            max_tokens=1000
        )

    def clasificar_mensaje(self, mensaje, historial=""):
        """El LLM decide si es conversación casual o consulta técnica"""
        prompt_clasificador = ChatPromptTemplate.from_template("""
Analiza este mensaje de un estudiante universitario y determina si es:
1. CASUAL - conversación normal, saludos, preguntas personales, charla general
2. TECNICA - consulta específica sobre trámites, fechas, procedimientos académicos

HISTORIAL RECIENTE:
{historial}

MENSAJE: "{mensaje}"

Responde SOLO con: CASUAL o TECNICA
""")
        
        respuesta = self.llm_clasificador.invoke(
            prompt_clasificador.format(mensaje=mensaje, historial=historial)
        ).content.strip().upper()
        
        return "CASUAL" in respuesta

    def responder_casual(self, mensaje, historial):
        """Respuesta conversacional natural"""
        prompt_casual = ChatPromptTemplate.from_template("""
Eres un asistente amigable de la Facultad de Ingeniería Eléctrica y Electrónica (FIEE-UNI).

Responde de manera natural y conversacional. No uses listas ni bullet points para conversación casual.
Sé como un estudiante senior amigable que está ahí para ayudar.

CONVERSACIÓN PREVIA:
{historial}

MENSAJE DEL ESTUDIANTE: {mensaje}

Responde de manera natural y amigable:""")
        
        return self.llm_conversacional.invoke(
            prompt_casual.format(mensaje=mensaje, historial=historial)
        ).content

    def responder_tecnico(self, mensaje, docs, historial):
        """Respuesta técnica basada en documentos"""
        contexto = self.formatear_documentos(docs)
        
        prompt_tecnico = ChatPromptTemplate.from_template("""
Eres un asistente especializado de la FIEE-UNI. Responde de manera profesional pero cercana.

INFORMACIÓN DISPONIBLE:
{contexto}

CONVERSACIÓN PREVIA:
{historial}

CONSULTA: {mensaje}

Instrucciones IMPORTANTES:
- Usa SOLO la información proporcionada
- Para TRÁMITES: Da pasos específicos, procedimientos detallados y requisitos
- Para DOCUMENTOS: Explica qué necesita, dónde presentarlo y costos
- Para PAGOS: Da instrucciones paso a paso del proceso
- Enumera los pasos cuando sea un procedimiento
- Sé específico con requisitos y documentos necesarios
- Mantén un tono profesional pero amigable
- Si no tienes la información completa, dilo claramente

Respuesta con pasos específicos:""")
        
        return self.llm_tecnico.invoke(prompt_tecnico.format(
            mensaje=mensaje,
            contexto=contexto,
            historial=historial
        )).content

    def formatear_documentos(self, docs):
        """Formatea documentos de manera simple"""
        if not docs:
            return "No se encontró información específica."
        
        contexto = []
        for doc in docs[:3]:  # Solo los 3 más relevantes
            filename = doc.metadata.get('filename', 'Documento')
            contenido = doc.page_content[:600]
            contexto.append(f"Documento: {filename}\nContenido: {contenido}\n")
        
        return "\n".join(contexto)

def buscar_documentos(db, query, k=5):
    """Búsqueda simple en la base de datos"""
    try:
        # Expandir query solo para términos muy específicos
        if any(term in query.lower() for term in ['matricula', 'examen', 'retiro', 'traslado']):
            expansiones = {
                'matricula': ' inscripcion registro',
                'examen': ' evaluacion prueba',
                'retiro': ' abandono',
                'traslado': ' cambio transferencia'
            }
            for term, expansion in expansiones.items():
                if term in query.lower():
                    query += expansion
        
        docs = db.similarity_search(query, k=k)
        return docs
    except Exception:
        return []

def formatear_historial(chat_history):
    """Formatea historial de manera natural"""
    if not chat_history:
        return "Primera conversación"
    
    # Solo las últimas 2 interacciones
    reciente = chat_history[-4:] if len(chat_history) > 4 else chat_history
    
    historial = []
    for i in range(0, len(reciente), 2):
        if i + 1 < len(reciente):
            historial.append(f"Estudiante: {reciente[i]}")
            historial.append(f"Asistente: {reciente[i + 1]}")
    
    return "\n".join(historial)

def main():
    print("🎓 Inicializando Asistente FIEE-UNI...")
    
    # Inicializar chatbot
    chatbot = ChatbotNatural()
    
    # Cargar base de datos
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    try:
        db = FAISS.load_local("vector_db_imagenes", embeddings, allow_dangerous_deserialization=True)
        print("✅ Base de datos cargada")
    except Exception as e:
        print(f"⚠️ Sin base de datos: {e}")
        db = None
    
    # Historial de conversación
    chat_history = []
    
    print("\n🤖 ¡Hola! Soy tu asistente de la FIEE 😊")
    print("💡 Escribe 'salir' para terminar\n")

    while True:
        query = input("👤 Tú: ").strip()
        
        if query.lower() in ["salir", "exit", "quit"]:
            print("\n👋 ¡Hasta luego!")
            break
            
        if not query:
            continue
            
        try:
            # Formatear historial
            historial = formatear_historial(chat_history)
            
            # El LLM decide el tipo de conversación
            es_casual = chatbot.clasificar_mensaje(query, historial)
            
            if es_casual:
                # Conversación casual
                response = chatbot.responder_casual(query, historial)
                print(f"\n🤖 {response}\n")
                
            else:
                # Consulta técnica
                if db is None:
                    response = "Disculpa, no tengo acceso a la información técnica en este momento, pero podemos seguir conversando 😊"
                    print(f"\n🤖 {response}\n")
                else:
                    print("🔍 Buscando información...")
                    docs = buscar_documentos(db, query)
                    
                    if docs:
                        response = chatbot.responder_tecnico(query, docs, historial)
                        print(f"\n🎓 {response}")
                        
                        # Mostrar fuentes discretamente
                        print(f"\n📚 Información de: {docs[0].metadata.get('filename', 'documentos oficiales')}")
                        if len(docs) > 1:
                            print(f"    y {len(docs)-1} documento(s) más\n")
                        else:
                            print()
                    else:
                        response = "No encontré información específica sobre eso. ¿Podrías darme más detalles?"
                        print(f"\n🤖 {response}\n")
            
            # Actualizar historial
            chat_history.append(query)
            chat_history.append(response)
            
            # Mantener solo las últimas 6 interacciones
            if len(chat_history) > 6:
                chat_history = chat_history[-6:]
                
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            # Respuesta de fallback natural
            fallback_response = "Disculpa, tuve un pequeño problema. ¿Puedes repetir eso?"
            print(f"🤖 {fallback_response}\n")

if __name__ == "__main__":
    main()