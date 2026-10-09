# Aplicação FastAPI

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas, database

# Cria as tabelas no SQLite
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="API Futebol")

# Permite chamadas vindas do Angular (http://localhost:4200)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensagem": "API de Futebol com FastAPI rodando com sucesso!"}

@app.get("/api/times", response_model=List[schemas.TimeResponse])
def listar_times(db: Session = Depends(database.get_db)):
    return db.query(models.Time).all()

@app.post("/api/times", response_model=schemas.TimeResponse)
def criar_time(time: schemas.TimeCreate, db: Session = Depends(database.get_db)):
    novo_time = models.Time(nome=time.nome, estado=time.estado)
    db.add(novo_time)
    db.commit()
    db.refresh(novo_time)
    return novo_time