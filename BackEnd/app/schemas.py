# Validações do Pydantic

from pydantic import BaseModel, field_validator
from app.models import Clube


class ClubeCreate(Clube):
    """Dados validados recebidos do formulário de cadastro de clube."""

    @field_validator("website", "escudo", mode="before")
    @classmethod
    def strings_vazias_sao_nulas(cls, valor):
        return None if valor == "" else valor
