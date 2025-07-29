from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
docs_store = []

def build_vector_store(docs):
    global docs_store
    embeddings = model.encode(docs)
    index.reset() 
    index.add(np.array(embeddings))
    docs_store = docs

def get_relevant_chunks(query, k=3):
    if index.ntotal == 0:
        print("⚠️ FAISS index is empty.")
        return []

    query_vec = model.encode([query])
    _, indices = index.search(query_vec, k)

    results = []
    for i in indices[0]:
        if 0 <= i < len(docs_store):
            results.append(docs_store[i])
    return results

