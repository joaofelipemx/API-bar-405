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



# CLIENTE
async def criar_cliente(db: AsyncSession, cliente: schemas.ClienteCreate):
    novo_cliente = models.Cliente(**cliente.model_dump())
    db.add(novo_cliente)
    await db.commit()
    await db.refresh(novo_cliente)
    return novo_cliente
async def listar_clientes(db: AsyncSession):
    result = await db.execute(select(models.Cliente))
    return result.scalars().all()
async def buscar_cliente(db: AsyncSession, cliente_id: int):
    result = await db.execute(
        select(models.Cliente).where(models.Cliente.id == cliente_id)
    )
    return result.scalar_one_or_none()
async def atualizar_cliente(db: AsyncSession, cliente_id: int, dados: schemas.ClienteCreate):
    cliente = await buscar_cliente(db, cliente_id)
    if cliente is None:
        return None
    cliente.nome = dados.nome
    cliente.telefone = dados.telefone
    await db.commit()
    await db.refresh(cliente)
    return cliente
async def deletar_cliente(db: AsyncSession, cliente_id: int):
    cliente = await buscar_cliente(db, cliente_id)
    if cliente is None:
        return None
    await db.delete(cliente)
    await db.commit()
    return cliente



#PRODUTO
async def criar_produto(db: AsyncSession, produto: schemas.ProdutoCreate):
    categoria = await buscar_categoria(db, produto.categoria_id)
    if categoria is None:
        return None
    novo_produto = models.Produto(**produto.model_dump())
    db.add(novo_produto)
    await db.commit()
    await db.refresh(novo_produto)
    return novo_produto
async def listar_produtos(db: AsyncSession):
    result = await db.execute(select(models.Produto))
    return result.scalars().all()
async def buscar_produto(db: AsyncSession, produto_id: int):
    result = await db.execute(
        select(models.Produto).where(models.Produto.id == produto_id)
    )
    return result.scalar_one_or_none()
async def atualizar_produto(db: AsyncSession, produto_id: int, dados: schemas.ProdutoCreate):
    produto = await buscar_produto(db, produto_id)
    if produto is None:
        return None
    categoria = await buscar_categoria(db, dados.categoria_id)
    if categoria is None:
        return "Categoria inválida"
    produto.nome = dados.nome
    produto.estoque = dados.estoque
    produto.preco = dados.preco
    produto.categoria_id = dados.categoria_id
    await db.commit()
    await db.refresh(produto)
    return produto
async def deletar_produto(db: AsyncSession, produto_id: int):
    produto = await buscar_produto(db, produto_id)
    if produto is None:
        return None
    await db.delete(produto)
    await db.commit()
    return produto