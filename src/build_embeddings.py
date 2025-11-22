import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os

DATA_PATH = "data/facts.csv"
MODEL_PATH = "models/vector_store.faiss"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def build_vector_db():
    print("Loading data...")
    df = pd.read_csv(DATA_PATH)

    print("Generating embeddings...")
    model = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = model.encode(df['fact'].tolist(), convert_to_numpy=True)

    print("Saving FAISS index...")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    os.makedirs("models", exist_ok=True)
    faiss.write_index(index, MODEL_PATH)

    print("Vector DB Created Successfully!")

if __name__ == "__main__":
    build_vector_db()
