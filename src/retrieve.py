import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

MODEL_PATH = "models/vector_store.faiss"
DATA_PATH = "data/facts.csv"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def retrieve_similar_fact(claim, k=3):
    df = pd.read_csv(DATA_PATH)
    index = faiss.read_index(MODEL_PATH)

    model = SentenceTransformer(EMBEDDING_MODEL)
    vector = model.encode([claim])

    distances, indices = index.search(np.array(vector), k)

    results = []
    for i, dist in zip(indices[0], distances[0]):
        results.append({"fact": df.iloc[i]['fact'], "score": float(dist)})

    return results

if __name__ == "__main__":
    print(retrieve_similar_fact("Paris is the capital of Spain."))
