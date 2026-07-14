from fastapi import FastAPI
from routers import categoria, cliente, produto, pedido, item_pedido, usuario 

app = FastAPI(title="Bar 405 API")

app.include_router(categoria.router)
app.include_router(cliente.router)
app.include_router(produto.router)
app.include_router(pedido.router)
app.include_router(item_pedido.router)
app.include_router(usuario.router)