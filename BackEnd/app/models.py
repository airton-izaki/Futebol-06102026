# Tabelas (Times, Jogadores, Partidas)

from sqlalchemy import Column, Integer, String
from app.database import Base

class Time(Base):
    __tablename__ = "times"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    estado = Column(String(2), nullable=False)