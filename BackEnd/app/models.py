# Tabelas (Times, Jogadores, Partidas)
from pydantic       import BaseModel, HttpUrl, Field, ConfigDict
from typing         import Optional
from datetime       import datetime, date
from enum           import Enum

class GestaoEnum(str, Enum):
    ASSOCIATIVO = "Associativo"
    SAF = "SAF"
    PRIVADO = "Privado"
    HÍBRIDO = "Híbrido"

class Clube(BaseModel):
    nome_oficial: str = Field(..., max_length = 100)
    nome: str = Field(..., max_length = 100)
    sigla: str = Field(..., max_length = 5)
    gestao: GestaoEnum = GestaoEnum.ASSOCIATIVO
    fundacao: date
    estado: str = Field(..., min_length = 2, max_length = 50, description = "UF (ex: São Paulo)")
    cidade: str = Field(..., max_length = 100, description = "Nome da cidade")
    estadio: Optional[str] = Field(default = "", max_length = 100)
    cor_primaria: str = Field(..., max_length = 30)
    cor_secundaria: Optional[str] = Field(default = "", max_length = 30)
    cor_terciaria: Optional[str] = Field(default = "", max_length = 30)
    website: Optional[HttpUrl] = None
    escudo: Optional[HttpUrl] = None
    observacao: Optional[str] = ""
    ativo: bool = True

class ClubeResponse(Clube):
    id: int
    criado_em: datetime
    atualizado_em: datetime

    model_config = ConfigDict(from_attributes = True)






































