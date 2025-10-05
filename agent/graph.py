from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict, Any
from models.llm import get_llm
from agent.tools import tool_retrieve_guideline, tool_extract_and_score


class S(TypedDict):
    question: str
    html_report: str
    context: List[Dict[str,Any]]
    answer: str
    form: Dict[str,Any]


llm = get_llm()


def retrieve_node(state:S)->S:
    ctx = tool_retrieve_guideline(state["question"])
    return {**state, "context": ctx}


def score_node(state:S)->S:
    out = tool_extract_and_score(state["html_report"])
    return {**state, "form": out["form"]}


def answer_node(state:S)->S:
    system = (
        "Eres un asistente clínico. Responde SOLO con base en los fragmentos 'Contexto'. "
        "Incluye citas [source:page] y NO inventes. Si falta evidencia, dilo explícitamente."
    )
    ctx_txt = "\n---\n".join([f"({i}) {c['text']}\n[source:{c.get('source')} page:{c.get('page')}]" for i,c in enumerate(state["context"],1)])
    prompt = f"{system}\n\nContexto:\n{ctx_txt}\n\nPregunta: {state['question']}"
    msg = llm.invoke(prompt)
    return {**state, "answer": msg.content}


def build_graph():
    g = StateGraph(S)
    g.add_node("retrieve", retrieve_node)
    g.add_node("score", score_node)
    g.add_node("answer", answer_node)
    g.set_entry_point("retrieve")
    g.add_edge("retrieve","score")
    g.add_edge("score","answer")
    g.add_edge("answer", END)
    return g.compile()