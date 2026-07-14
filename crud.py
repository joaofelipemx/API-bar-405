from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import models
import schemas
from security import hash_senha, verificar_senha

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

#PEDIDOS
async def criar_pedido(db: AsyncSession, pedido: schemas.PedidoCreate):
    novo_pedido = models.Pedido(**pedido.model_dump())
    cliente = await buscar_cliente(db, novo_pedido.cliente_id)
    if cliente is None:
        return None
    db.add(novo_pedido)
    await db.commit()
    await db.refresh(novo_pedido)
    return novo_pedido
async def listar_pedidos(db: AsyncSession):
    result = await db.execute(select(models.Pedido))
    return result.scalars().all()
async def buscar_pedido(db: AsyncSession, pedido_id: int):
    result = await db.execute(
        select(models.Pedido).where(models.Pedido.id == pedido_id)
    )
    return result.scalar_one_or_none()
async def atualizar_pedido(db: AsyncSession, pedido_id: int, dados: schemas.PedidoCreate):
    pedido = await buscar_pedido(db, pedido_id)
    if pedido is None:
        return None
    cliente = await buscar_cliente(db, dados.cliente_id)
    if cliente is None:
        return "cliente invalido"
    pedido.cliente_id = dados.cliente_id
    pedido.data = dados.data
    pedido.status = dados.status
    await db.commit()
    await db.refresh(pedido)
    return pedido
async def deletar_pedido(db: AsyncSession, pedido_id: int):
    pedido = await buscar_pedido(db, pedido_id)
    if pedido is None:
        return None
    await db.delete(pedido)
    await db.commit()
    return pedido


#ItemPedido
async def criar_item_pedido(db: AsyncSession, item_pedido: schemas.ItemPedidoCreate):
    novo_item = models.ItemPedido(**item_pedido.model_dump())
    pedido = await buscar_pedido(db, novo_item.pedido_id)
    if pedido is None:
        return "pedido invalido"
    produto = await buscar_produto(db, novo_item.produto_id)
    if produto is None:
        return "produto invalido"
    db.add(novo_item)
    await db.commit()
    await db.refresh(novo_item)
    return novo_item
async def listar_itens_pedido(db: AsyncSession):
    result = await db.execute(select(models.ItemPedido))
    return result.scalars().all()
async def buscar_item_pedido(db: AsyncSession, item_id: int):
    item = await db.execute(
        select(models.ItemPedido).where(models.ItemPedido.id == item_id)
    )
    return item.scalar_one_or_none()
async def atualizar_item_pedido(db: AsyncSession, item_id: int, dados: schemas.ItemPedidoCreate):
    item_pedido = await buscar_item_pedido(db, item_id)
    if item_pedido is None:
        return None
    pedido = await buscar_pedido(db, dados.pedido_id)
    if pedido is None:
        return "pedido invalido"
    produto = await buscar_produto(db, dados.produto_id)
    if produto is None:
        return "produto invalido"
    item_pedido.pedido_id = dados.pedido_id
    item_pedido.produto_id = dados.produto_id
    item_pedido.quantidade = dados.quantidade
    item_pedido.preco_unitario = dados.preco_unitario
    await db.commit()
    await db.refresh(item_pedido)
    return item_pedido
async def deletar_item_pedido(db: AsyncSession, item_id: int):
    item_pedido = await buscar_item_pedido(db, item_id)
    if item_pedido is None:
        return None
    await db.delete(item_pedido)
    await db.commit()
    return item_pedido


#USUARIO
async def criar_usuario(db: AsyncSession, usuario: schemas.UsuarioCreate):
    senha_hash = hash_senha(usuario.password)
    novo_usuario = models.Usuario(
        username=usuario.username,
        email=usuario.email,
        password_hash=senha_hash
    )
    db.add(novo_usuario)
    await db.commit()
    await db.refresh(novo_usuario)
    return novo_usuario
async def buscar_usuario_por_username(db: AsyncSession, username: str):
    resultado = await db.execute(
        select(models.Usuario).where(models.Usuario.username == username)
    )
    return resultado.scalar_one_or_none()