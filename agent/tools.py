from rag.retriever import load_retriever
from ie.extractors import extract_vars_from_html
from ie.schemas import WellsForm
from ie.scores import compute_wells


_retriever = None


def _get_retriever():
    global _retriever
    if _retriever is None:
        _retriever = load_retriever()
    return _retriever


def tool_retrieve_guideline(q:str):
    docs = _get_retriever().get_relevant_documents(q)
    return [{"page": d.metadata.get("page"), "source": d.metadata.get("source"), "text": d.page_content} for d in docs]


def tool_extract_and_score(html:str, overrides:dict|None=None):
    feats, raw = extract_vars_from_html(html)
    if overrides: feats.update(overrides)
    form = compute_wells(WellsForm(**{k: bool(v) for k,v in feats.items()}))
    return {"form": form.model_dump(), "raw_text": raw[:2000]}

