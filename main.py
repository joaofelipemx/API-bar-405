from fastapi import FastAPI
from routers import categoria, cliente, produto, pedido

app = FastAPI(title="Bar 405 API")

app.include_router(categoria.router)
app.include_router(cliente.router)
app.include_router(produto.router)
app.include_router(pedido.router)