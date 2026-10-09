# Validações do Pydantic

from pydantic import BaseModel

class TimeBase(BaseModel):
    nome: str
    estado: str

class TimeCreate(TimeBase):
    pass

class TimeResponse(TimeBase):
    id: int

    class Config:
        from_attributes = True