# ie/schemas.py
from pydantic import BaseModel, Field
from typing import Optional, List

class WellsForm(BaseModel):
    patient_id: Optional[str] = None
    sospecha_tvp: bool
    taquicardia: bool
    inmovilizacion_reciente: bool
    antecedente_tvp: bool
    hemoptisis: bool
    cancer_activo: bool
    dolor_miembro_inferior: bool
    diagnostico_alternativo_mas_probable: bool
    score: int = Field(0)
    categoria: str