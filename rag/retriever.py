# rag/retriever.py
from langchain_community.vectorstores import FAISS
from models.embeddings import get_embeddings

def load_retriever(path="rag/vectorstore"):
    vs = FAISS.load_local(path, get_embeddings(), allow_dangerous_deserialization=True)
    return vs.as_retriever(search_type="mmr", search_kwargs={"k":4, "fetch_k":20, "lambda_mult":0.5})
