from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db_connection
import crud
import schemas

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/", response_model=schemas.PedidoResponse)
async def criar_pedido(pedido: schemas.PedidoCreate, db: AsyncSession = Depends(get_db_connection)):
    novo_pedido = await crud.criar_pedido(db, pedido)
    if novo_pedido is None:
        raise HTTPException(status_code=400, detail="cliente não existe")
    return novo_pedido

@router.get("/", response_model=list[schemas.PedidoResponse])
async def listar_pedidos(db: AsyncSession = Depends(get_db_connection)):
    return await crud.listar_pedidos(db)

@router.get("/{pedido_id}", response_model=schemas.PedidoResponse)
async def buscar_pedido(pedido_id: int, db: AsyncSession = Depends(get_db_connection)):
    pedido = await crud.buscar_pedido(db, pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@router.put("/{pedido_id}", response_model=schemas.PedidoResponse)
async def atualizar_pedido(pedido_id: int, dados: schemas.PedidoCreate, db: AsyncSession = Depends(get_db_connection)):
    pedido = await crud.atualizar_pedido(db, pedido_id, dados)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    if pedido == "cliente invalido":
        raise HTTPException(status_code=400, detail="Cliente não existe")
    return pedido

@router.delete("/{pedido_id}")
async def deletar_pedido(pedido_id: int, db: AsyncSession = Depends(get_db_connection)):
    pedido = await crud.deletar_pedido(db, pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido