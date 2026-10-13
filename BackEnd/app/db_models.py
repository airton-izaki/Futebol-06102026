"""SQLAlchemy models persisted in the database."""

from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Enum, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models import GestaoEnum


class ClubeDB(Base):
    __tablename__ = "clubes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome_oficial: Mapped[str] = mapped_column(String(100), nullable=False)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    sigla: Mapped[str] = mapped_column(String(5), nullable=False)
    gestao: Mapped[GestaoEnum] = mapped_column(
        Enum(GestaoEnum, native_enum=False, length=20),
        nullable=False,
        default=GestaoEnum.ASSOCIATIVO,
    )
    fundacao: Mapped[date] = mapped_column(Date, nullable=False)
    estado: Mapped[str] = mapped_column(String(50), nullable=False)
    cidade: Mapped[str] = mapped_column(String(100), nullable=False)
    estadio: Mapped[str | None] = mapped_column(String(100), nullable=True, default="")
    cor_primaria: Mapped[str] = mapped_column(String(30), nullable=False)
    cor_secundaria: Mapped[str | None] = mapped_column(String(30), nullable=True, default="")
    cor_terciaria: Mapped[str | None] = mapped_column(String(30), nullable=True, default="")
    website: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    escudo: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    observacao: Mapped[str | None] = mapped_column(Text, nullable=True, default="")
    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    criado_em: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )
