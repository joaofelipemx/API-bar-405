from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import models
import schemas

# CATEGORIA
async def criar_categoria(db: AsyncSession, categoria: schemas.CategoriaCreate):
    nova_categoria = models.Categoria(**categoria.model_dump())
    db.add(nova_categoria)
    await db.commit()
    await db.refresh(nova_categoria)
    return nova_categoria

async def listar_categorias(db: AsyncSession):
    result = await db.execute(select(models.Categoria))
    return result.scalars().all()

async def buscar_categoria(db:AsyncSession, categoria_id: int):
    result = await db.execute(
        select(models.Categoria).where(models.Categoria.id == categoria_id)
    )
    return result.scalar_one_or_none()

async def atualizar_categoria(db: AsyncSession, categoria_id: int, dados: schemas.CategoriaCreate):
    categoria = await buscar_categoria(db, categoria_id)
    if categoria is None:
        return None
    categoria.nome = dados.nome
    await db.commit()
    await db.refresh(categoria)
    return categoria

async def deletar_cateria(db: AsyncSession, categoria_id: int):
    categoria = await buscar_categoria(db, categoria_id)
    if categoria is None:
        return None
    await db.delete(categoria)
    await db.commit()
    return categoria

