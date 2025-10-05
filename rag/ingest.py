# rag/ingest.py
from langchain_community.document_loaders import UnstructuredHTMLLoader, PyPDFLoader, CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from models.embeddings import get_embeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path

def load_docs(paths):
    docs=[]
    for p in paths:
        p=Path(p)
        if p.suffix.lower()==".pdf":
            docs+=PyPDFLoader(str(p)).load()
        elif p.suffix.lower() in [".html",".htm"]:
            docs+=UnstructuredHTMLLoader(str(p)).load()
        elif p.suffix.lower()==".csv":
            docs+=CSVLoader(str(p)).load()
    return docs

def build_index(paths, out_dir="rag/vectorstore"):
    docs = load_docs(paths)
    splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=150)
    chunks = splitter.split_documents(docs)
    vs = FAISS.from_documents(chunks, get_embeddings())
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    vs.save_local(out_dir)
    return out_dir

if __name__ == "__main__":
    import sys; build_index(sys.argv[1:])
