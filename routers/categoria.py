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