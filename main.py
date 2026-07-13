from fastapi import FastAPI
from routers import categoria, cliente

app = FastAPI(title="Bar 405 API")

app.include_router(categoria.router)
app.include_router(cliente.router)
