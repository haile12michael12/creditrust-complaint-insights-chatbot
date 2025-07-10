import pandas as pd
import numpy as np
import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load data
df = pd.read_csv("data/complaints_cleaned.csv")

# Text chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks, metadata = [], []
for _, row in df.iterrows():
    complaint_id = row["complaint_id"]
    product = row["product"]
    text = row["narrative"]
    
    split_texts = splitter.split_text(text)
    for chunk in split_texts:
        chunks.append(chunk)
        metadata.append({
            "text": chunk,
            "complaint_id": complaint_id,
            "product": product
        })

# Embedding
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks, batch_size=32, show_progress_bar=True)
embedding_matrix = np.array(embeddings).astype("float32")

# Create FAISS index
index = faiss.IndexFlatL2(embedding_matrix.shape[1])
index.add(embedding_matrix)

# Save vector store
os.makedirs("vector_store", exist_ok=True)
faiss.write_index(index, "vector_store/faiss_index.index")
with open("vector_store/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)
