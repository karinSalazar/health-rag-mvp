# ie/extractors.py
import re
from bs4 import BeautifulSoup

SIGN_PATTERNS = {
    "taquicardia": r"(FC|frecuencia cardi(aca|aca)|taquicardia)\D{0,10}(\b(>?\s?100|min)|\btaquicardia\b)",
    "hemoptisis": r"\bhemopt(isis|oe)\b",
    "cancer_activo": r"\b(c[áa]ncer|neoplasia)( activa)?\b",
    "inmovilizacion_reciente": r"(inmovilizaci[óo]n|cirug[íi]a)\b.{0,30}\b(3|4|sem|semana|d[ií]as)",
    "antecedente_tvp": r"(antecedente|historia).{0,15}\bTVP\b",
    "dolor_miembro_inferior": r"\bdolor\b.{0,30}\b(pierna|miembro inferior)\b"
}

def extract_vars_from_html(html:str)->dict:
    soup = BeautifulSoup(html, "html.parser")
    text = re.sub(r"\s+"," ", soup.get_text(" ", strip=True), flags=re.M)
    feats = {k: bool(re.search(p, text, flags=re.I)) for k,p in SIGN_PATTERNS.items()}
    # este lo dejamos a decisión clínica del redactor (el agente lo preguntará si falta)
    feats.setdefault("sospecha_tvp", "tvp" in text.lower())
    feats.setdefault("diagnostico_alternativo_mas_probable", False)
    return feats, text

