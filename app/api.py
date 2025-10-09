from fastapi import FastAPI
from pydantic import BaseModel
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent.graph import build_graph


app = FastAPI(title="Health RAG MVP")


class Query(BaseModel):
    question: str
    html_report: str


@app.post("/ask")
def ask(q: Query):
    g = build_graph()
    out = g.invoke({"question": q.question, "html_report": q.html_report, "context": [], "answer": "", "form": {}})
    return out