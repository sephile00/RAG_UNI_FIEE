import os
import json
import easyocr
import fitz  

reader = easyocr.Reader(['es'])  
folder_path = "./data"

results = []

if not os.path.exists(folder_path):
    print(f"Error: La carpeta {folder_path} no existe.")
    exit(1)

processed_files = 0
total_images = 0
total_pdfs = 0

for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)
    
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        total_images += 1
        print(f"Procesando imagen: {filename}")
        
        try:
            result = reader.readtext(filepath)
            text = " ".join([res[1] for res in result])
            if text.strip():
                results.append({
                    "filename": filename,
                    "texto": text,
                    "ruta": filepath,
                    "tipo": "imagen"
                })
                processed_files += 1
                print(f"Texto extraído exitosamente ({len(text)} caracteres)")
            else:
                print("No se pudo extraer texto de la imagen")
                
        except Exception as e:
            print(f"Error al procesar {filename}: {str(e)}")
    
    elif filename.lower().endswith(".pdf"):
        total_pdfs += 1
        print(f"Procesando PDF: {filename}")
        
        try:

            pdf_document = fitz.open(filepath)

            text = ""
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                text += page.get_text()

            pdf_document.close()

            if text.strip():
                results.append({
                    "filename": filename,
                    "texto": text,
                    "ruta": filepath,
                    "tipo": "pdf"
                })
                processed_files += 1
                print(f"Texto extraído exitosamente ({len(text)} caracteres)")
            else:
                print("No se pudo extraer texto del PDF")
                
        except Exception as e:
            print(f"Error al procesar {filename}: {str(e)}")


if results:
    output_file = "textos_extraidos.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nResumen:")
    print(f"Total de imágenes encontradas: {total_images}")
    print(f"Total de PDFs encontrados: {total_pdfs}")
    print(f"Archivos procesados exitosamente: {processed_files}")
    print(f"Resultados guardados en '{output_file}'")
else:
    print("\nNo se pudo extraer texto de ningún archivo.")