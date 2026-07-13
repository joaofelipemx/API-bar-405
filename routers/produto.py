from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db_connection
import crud
import schemas

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/", response_model=schemas.ProdutoResponse)
async def criar_produto(produto: schemas.ProdutoCreate, db: AsyncSession = Depends(get_db_connection)):
    novo_produto = await crud.criar_produto(db, produto)
    if novo_produto is None:
        raise HTTPException(status_code=400, detail="Categoria não existe")
    return novo_produto

@router.get("/", response_model=list[schemas.ProdutoResponse])
async def listar_produtos(db: AsyncSession = Depends(get_db_connection)):
    return await crud.listar_produtos(db)

@router.get("/{produto_id}", response_model=schemas.ProdutoResponse)
async def buscar_produto(produto_id: int, db: AsyncSession = Depends(get_db_connection)):
    produto = await crud.buscar_produto(db, produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/{produto_id}", response_model=schemas.ProdutoResponse)
async def atualizar_produto(produto_id: int, dados: schemas.ProdutoCreate, db: AsyncSession = Depends(get_db_connection)):
    produto = await crud.atualizar_produto(db, produto_id, dados)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if produto == "categoria_invalida":
        raise HTTPException(status_code=400, detail="Categoria não existe")
    return produto

@router.delete("/{produto_id}")
async def deletar_produto(produto_id: int, db: AsyncSession = Depends(get_db_connection)):
    resultado = await crud.deletar_produto(db, produto_id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return resultado