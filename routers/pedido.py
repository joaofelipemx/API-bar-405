from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db_connection
import crud
import schemas

router = APIRouter(prefix="/produtos", tags=["Produtos"])