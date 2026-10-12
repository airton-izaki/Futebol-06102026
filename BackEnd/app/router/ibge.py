import httpx
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List



# 1. Criação do Router
router_ibge = APIRouter(prefix = "/ibge", tags = ["IBGE"])

IBGE_ESTADOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome"
IBGE_CIDADES_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"

class EstadoResponse(BaseModel):
    id: int
    sigla: str
    nome: str

class CidadeResponse(BaseModel):
    id: int
    nome: str

@router_ibge.get("/estados", response_model=List[EstadoResponse])
async def listar_estados_ibge():
    """Busca a lista de todos os estados brasileiros no IBGE ordenados por nome."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(IBGE_ESTADOS_URL)
            response.raise_for_status()
            return [{"id": uf["id"], "sigla": uf["sigla"], "nome": uf["nome"]} for uf in response.json()]
        except httpx.HTTPError:
            raise HTTPException(status_code = 502, detail = "Erro ao comunicar com a API do IBGE.")

@router_ibge.get("/estados/{uf}/cidades", response_model=List[CidadeResponse])
async def listar_cidades_ibge(uf: str):
    """Busca todas as cidades de um determinado estado (ex: SP, RJ) no IBGE."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(IBGE_CIDADES_URL.format(uf = uf.upper()))
            if response.status_code == 404:
                raise HTTPException(status_code = 404, detail = f"Estado '{uf.upper()}' não encontrado.")
            response.raise_for_status()
            return [{"id": cidade["id"], "nome": cidade["nome"]} for cidade in response.json()]
        except httpx.HTTPError:
            raise HTTPException(status_code = 502, detail = "Erro ao comunicar com a API do IBGE.")
