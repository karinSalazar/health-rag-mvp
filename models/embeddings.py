# models/embeddings.py
from langchain_huggingface import HuggingFaceEmbeddings


def get_embeddings():
    model = "intfloat/multilingual-e5-small"
    return HuggingFaceEmbeddings(model_name=model, encode_kwargs={"normalize_embeddings": True})
