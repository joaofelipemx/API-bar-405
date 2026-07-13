from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db_connection
import crud
import schemas

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=schemas.ClienteResponse)
async def criar_cliente(cliente: schemas.ClienteCreate, db: AsyncSession = Depends(get_db_connection)):
    return await crud.criar_cliente(db, cliente)

@router.get("/", response_model=list[schemas.ClienteResponse])
async def listar_clientes(db: AsyncSession = Depends(get_db_connection)):
    return await crud.listar_clientes(db)

@router.get("/{cliente_id}", response_model=schemas.ClienteResponse)
async def buscar_cliente(cliente_id: int, db: AsyncSession = Depends(get_db_connection)):
    cliente = await crud.buscar_cliente(db, cliente_id)
    if cliente is None: 
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return cliente

@router.put("/{cliente_id}", response_model=schemas.ClienteResponse)
async def atualizar_cliente(cliente_id: int, dados: schemas.ClienteCreate, db: AsyncSession = Depends(get_db_connection)):
    cliente = await crud.atualizar_cliente(db, cliente_id, dados)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return cliente

@router.delete("/{cliente_id}")
async def deletar_cliente(cliente_id: int, db: AsyncSession =  Depends(get_db_connection)):
    cliente = await crud.deletar_cliente(db, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return cliente