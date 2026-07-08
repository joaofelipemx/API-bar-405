from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UsuarioCreate(BaseModel):
    username: str
    email: str
    password: str
class UsuarioResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class CategoriaCreate(BaseModel):
    nome: str
class CategoriaResponse(BaseModel):
    id: int
    nome: str

    model_config = ConfigDict(from_attributes=True)

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    estoque: int
    categoria_id: int
class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    estoque: int
    categoria_id: int

    model_config = ConfigDict(from_attributes=True)

class ClienteCreate(BaseModel):
    nome: str
    telefone: str
class ClienteResponse(BaseModel):
    id: int
    nome: str
    telefone: str

    model_config = ConfigDict(from_attributes=True)

class PedidoCreate(BaseModel):
    data: datetime
    status: str
    cliente_id: int
class PedidoResponse(BaseModel):
    id: int
    data: datetime
    status: str
    cliente_id: int

    model_config = ConfigDict(from_attributes=True)

class ItemPedidoCreate(BaseModel):
    quantidade: int
    preco_unitario: float
    produto_id: int
    pedido_id: int
class ItemPedidoResponse(BaseModel):
    id: int
    pedido_id: int
    produto_id: int
    quantidade: int
    preco_unitario: float

    model_config = ConfigDict(from_attributes=True)