# BackEnd/app/router/clube_db.py
import logging

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import get_db
from app.db_models import ClubeDB
from app.models import ClubeResponse
from app.schemas import ClubeCreate

router_clube_db = APIRouter(prefix = "/clubes", tags = ["Clubes"])
logger = logging.getLogger(__name__)


@router_clube_db.get("/{clube_id}", response_model=ClubeResponse)
def buscar_clube(clube_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    """Busca um clube pelo ID."""
    clube = db.get(ClubeDB, clube_id)
    if clube is None:
        raise HTTPException(status_code=404, detail="Clube não encontrado.")
    return clube


@router_clube_db.get("/", response_model=list[ClubeResponse])
def listar_clubes(db: Session = Depends(get_db)):
    """Retorna os clubes cadastrados, em ordem alfabética."""
    try:
        return db.query(ClubeDB).order_by(ClubeDB.nome.asc()).all()
    except SQLAlchemyError as exc:
        logger.exception("Falha ao consultar clubes no banco de dados.")
        raise HTTPException(
            status_code=500,
            detail="Não foi possível consultar os clubes.",
        ) from exc


@router_clube_db.post(
    "/",
    response_model=ClubeResponse,
    status_code=status.HTTP_201_CREATED,
)
def receber_clube(dados: ClubeCreate, db: Session = Depends(get_db)):
    """Valida e grava o cadastro do clube no banco."""
    valores = dados.model_dump()
    for campo_url in ("website", "escudo"):
        if valores[campo_url] is not None:
            valores[campo_url] = str(valores[campo_url])

    clube = ClubeDB(**valores)
    db.add(clube)
    try:
        db.commit()
        db.refresh(clube)
    except SQLAlchemyError as exc:
        db.rollback()
        logger.exception("Falha ao salvar clube no banco de dados.")
        raise HTTPException(
            status_code=500,
            detail="Não foi possível salvar o clube.",
        ) from exc

    return clube


@router_clube_db.put(
    "/{clube_id}",
    response_model=ClubeResponse,
    status_code=status.HTTP_200_OK,
)
def atualizar_clube(
    dados: ClubeCreate,
    clube_id: int = Path(..., ge=1),
    db: Session = Depends(get_db),
):
    """Substitui os dados de um clube existente."""
    clube = db.get(ClubeDB, clube_id)
    if clube is None:
        raise HTTPException(status_code=404, detail="Clube não encontrado.")

    valores = dados.model_dump()
    for campo_url in ("website", "escudo"):
        if valores[campo_url] is not None:
            valores[campo_url] = str(valores[campo_url])

    for campo, valor in valores.items():
        setattr(clube, campo, valor)

    try:
        db.commit()
        db.refresh(clube)
    except SQLAlchemyError as exc:
        db.rollback()
        logger.exception("Falha ao atualizar clube no banco de dados.")
        raise HTTPException(
            status_code=500,
            detail="Não foi possível atualizar o clube.",
        ) from exc

    return clube
