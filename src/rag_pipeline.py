from sentence_transformers import SentenceTransformer
import faiss
import pickle
from transformers import pipeline

# Load resources
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("vector_store/faiss_index.index")
with open("vector_store/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

generator = pipeline("text-generation", model="gpt2", max_new_tokens=200)

# Retriever
def retrieve_top_k_chunks(question: str, k: int = 5):
    query_embedding = model.encode([question]).astype("float32")
    _, I = index.search(query_embedding, k)
    return [metadata[i] for i in I[0] if i < len(metadata)]

# Prompt template
PROMPT_TEMPLATE = """
You are a financial analyst assistant for CrediTrust. Your task is to answer questions about customer complaints.
Use the following retrieved complaint excerpts to formulate your answer.
If the context doesn't contain the answer, state that you don't have enough information.

Context:
{context}

Question: {question}
Answer:"""

# Generator
def generate_answer(question: str, retrieved_chunks: list):
    context = "\n---\n".join([chunk['text'] for chunk in retrieved_chunks])
    prompt = PROMPT_TEMPLATE.format(context=context, question=question)
    result = generator(prompt)[0]["generated_text"]
    return result.split("Answer:")[-1].strip()
