import json
from langchain.docstore.document import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd


with open("textos_extraidos.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

docs = [
    Document(page_content=item["texto"], metadata=item)
    for item in datos
    if item.get("texto", "").strip()
]

emb = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectors = emb.embed_documents([d.page_content for d in docs])

pca = PCA(n_components=2)
coords = pca.fit_transform(vectors)

df = pd.DataFrame(coords, columns=["PC1", "PC2"])
df["filename"] = [d.metadata["filename"] for d in docs]
print(df.head()) 

plt.figure(figsize=(8, 6))
plt.scatter(df["PC1"], df["PC2"])
for i, fn in enumerate(df["filename"]):
    plt.annotate(fn, (df["PC1"][i], df["PC2"][i]), fontsize=8)
plt.title("Visualización de Embeddings (PCA 2D)")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.tight_layout()
plt.show()
