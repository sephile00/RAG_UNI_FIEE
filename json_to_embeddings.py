import json
import os
import shutil
from tqdm import tqdm
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

vector_db_path = "vector_db_imagenes"

if os.path.exists(vector_db_path):
    shutil.rmtree(vector_db_path)
    print("Base de datos anterior eliminada.")

with open("textos_extraidos.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

docs = []
for item in tqdm(datos, desc="Procesando documentos"):
    texto = item.get("texto", "")
    metadata = {
        "filename": item.get("filename"),
        "ruta": item.get("ruta"),
        "tipo": item.get("tipo")
    }
    if texto.strip():
        docs.append(Document(page_content=texto, metadata=metadata))

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Generando embeddings y creando FAISS...")
db = FAISS.from_documents(list(tqdm(docs, desc="Embedding docs")), embeddings)

db.save_local("vector_db_imagenes")
print(f"{len(docs)} documentos guardados en FAISS.")