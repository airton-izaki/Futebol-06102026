from fastapi            import FastAPI
from app.router.ibge    import router_ibge

# 1. Instância principal do FastAPI
app = FastAPI(
    title = "API Principal",
    version = "0.1.0"
)

# 2. Incluir o router do IBGE na aplicação principal
app.include_router(router_ibge)
@app.get("/")
def raiz():
    return {"message": "API rodando com sucesso!"}





