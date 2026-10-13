from fastapi                    import FastAPI
from fastapi.middleware.cors    import CORSMiddleware
from app.router.ibge            import router_ibge
from app.router.clube_db        import router_clube_db



# 1. Instância principal do FastAPI
app = FastAPI(
    title = "API Principal",
    version = "0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://127.0.0.1:4200"],
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Incluir o router do IBGE na aplicação principal
app.include_router(router_ibge)
app.include_router(router_clube_db)
@app.get("/")
def raiz():
    return {"message": "API rodando com sucesso!"}





