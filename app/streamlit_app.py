import streamlit as st
from agent.graph import build_graph
from rag.ingest import build_index


st.set_page_config(page_title="Healthcare RAG MVP", layout="wide")
st.title("RAG Sanitario (MVP) – Guías + Informe HTML + Escala")


st.sidebar.header("Archivos")
up_guide = st.sidebar.file_uploader("Guía clínica (PDF/HTML/CSV)", type=["pdf","html","htm","csv"])
up_report = st.sidebar.file_uploader("Informe de alta (HTML)", type=["html","htm"])


if st.sidebar.button("Ingestar guía demo"):
    build_index(["data/guia_aterosclerosis_demo.html"])
    st.sidebar.success("Guía demo indexada.")


if st.sidebar.button("Ingestar guía subida") and up_guide:
    path = f"/tmp/{up_guide.name}"
    with open(path,"wb") as f: f.write(up_guide.read())
    build_index([path])
    st.sidebar.success("Guía subida indexada.")


q = st.text_input("Pregunta (ej.: 'Criterios diagnósticos y referencias')", "¿Cómo se calcula la escala de Wells y umbrales de riesgo?")


if st.button("Responder"):
    if up_report:
        html = up_report.read().decode("utf-8", errors="ignore")
    else:
        html = open("data/informe_alta_demo.html", "r", encoding="utf-8").read()
    g = build_graph()
    out = g.invoke({"question": q, "html_report": html, "context": [], "answer": "", "form": {}})
    st.subheader("Respuesta (con citas)")
    st.write(out["answer"])
    st.subheader("Formulario (Wells)")
    st.json(out["form"])
