from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import models
import schemas

# CATEGORIA
async def criar_categoria(db: AsyncSession, categoria: schemas.CategoriaCreate):
    