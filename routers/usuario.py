from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db_connection
from security import verificar_senha
import crud
import schemas

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/", response_model=schemas.UsuarioResponse)
async def criar_usuario(usuario: schemas.UsuarioCreate, db: AsyncSession = Depends(get_db_connection)):
    usuario_existente = await crud.buscar_usuario_por_username(db, usuario.username)
    if usuario_existente is not None:
        raise HTTPException(status_code=400, detail="Username já está em uso")
    return await crud.criar_usuario(db, usuario)

@router.post("/login")
async def login(dados: schemas.LoginRequest, db: AsyncSession = Depends(get_db_connection)):
    usuario = await crud.buscar_usuario_por_username(db, dados.username)
    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuario ou senha invalidos")
    senha_correta = verificar_senha(dados.password, usuario.password_hash)
    if not senha_correta:
        raise HTTPException(status_code=401, detail="Usuario ou senha invalidos")
    return {"mensagem": "Login realizado com sucesso", "username": usuario.username}