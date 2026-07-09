from fastapi import FastAPI
from routers import categoria

app = FastAPI(title="Bar 405 API")

app.include_router(categoria.router)


@app.get("/")
def raiz():
    return {"mensagem": "Bar 405 API rodando!"}