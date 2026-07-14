from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db_connection
import crud
import schemas

router = APIRouter(prefix="/item-pedido", tags=["ItemPedido"])

@router.post("/", response_model=schemas.ItemPedidoResponse)
async def criar_item_pedido(item_pedido: schemas.ItemPedidoCreate, db: AsyncSession = Depends(get_db_connection)):
    novo_item = await crud.criar_item_pedido(db, item_pedido)
    if novo_item == "pedido invalido":
        raise HTTPException(status_code=400, detail="Pedido não existe")
    if novo_item == "produto invalido":
        raise HTTPException(status_code=400, detail="Produto não existe")
    return novo_item

@router.get("/", response_model=list[schemas.ItemPedidoResponse])
async def listar_itens_pedido(db: AsyncSession = Depends(get_db_connection)):
    return await crud.listar_itens_pedido(db)

@router.get("/{item_id}", response_model=schemas.ItemPedidoResponse)
async def buscar_item_pedido(item_id: int, db:AsyncSession = Depends(get_db_connection)):
    item_pedido = await crud.buscar_item_pedido(db, item_id)
    if item_pedido is None:
        raise HTTPException(status_code=404, detail="item_pedido_invalido")
    return item_pedido

@router.put("/{item_id}", response_model=schemas.ItemPedidoResponse)
async def atualizar_item_pedido(item_id: int, dados: schemas.ItemPedidoCreate, db: AsyncSession = Depends(get_db_connection)):
    item_pedido = await crud.atualizar_item_pedido(db, item_id, dados)
    if item_pedido is None:
        raise HTTPException(status_code=404, detail="item_pedido_invalido")
    return item_pedido

@router.delete("/{item_id}")
async def deletar_item_pedido(item_id: int, db: AsyncSession = Depends(get_db_connection)):
    resultado = await crud.deletar_item_pedido(db, item_id)
    return resultado