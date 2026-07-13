from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db_connection
import crud
import schemas

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.post("/", response_model=schemas.CategoriaResponse)
async def criar_categoria(categoria: schemas.CategoriaCreate, db: AsyncSession = Depends(get_db_connection)):
    return await crud.criar_categoria(db, categoria)

@router.get("/", response_model=list[schemas.CategoriaResponse])
async def listar_categorias(db: AsyncSession = Depends(get_db_connection)):
    return await crud.listar_categorias(db)

@router.get("/{categoria_id}", response_model=schemas.CategoriaResponse)
async def buscar_categoria(categoria_id: int, db: AsyncSession = Depends(get_db_connection)):
    categoria = await crud.buscar_categoria(db, categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, datail="Categoria não encontrada.")
    return categoria

@router.put("/{categoria_id}", response_model=schemas.CategoriaResponse)
async def atualizar_categoria(categoria_id: int, dados: schemas.CategoriaResponse, db: AsyncSession = Depends(get_db_connection)):
    categoria = await crud.atualizar_categoria(db, categoria_id, dados)
    if categoria is None:
        raise HTTPException(status_code=404, datail="Categoria não encontrada.")
    return categoria

@router.delete("/{categoria_id}")
async def deletar_categoria(categoria_id: int, db: AsyncSession = Depends(get_db_connection)):
    categoria = await crud.deletar_cateria(db, categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria
    