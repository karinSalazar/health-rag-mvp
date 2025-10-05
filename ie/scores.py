# ie/scores.py
from ie.schemas import WellsForm

RULES = {
    "sospecha_tvp": 3, "taquicardia": 1.5, "inmovilizacion_reciente": 1.5,
    "antecedente_tvp": 1.5, "hemoptisis": 1, "cancer_activo": 1,
    "dolor_miembro_inferior": 3, "diagnostico_alternativo_mas_probable": -3
}
def compute_wells(form: WellsForm)->WellsForm:
    score = 0
    for k,v in RULES.items():
        score += v if getattr(form,k) else 0
    form.score = int(score) if float(score).is_integer() else round(score,1)
    form.categoria = "alto" if form.score>=6 else ("intermedio" if form.score>=2 else "bajo")
    return form