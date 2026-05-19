from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database.connection import get_db
from app.controllers.auth_controller import registrar_usuario, autenticar_usuario

router = APIRouter(prefix="/auth", tags=["Autenticação"])

class RegistroSchema(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: str = "empresa"

class LoginSchema(BaseModel):
    email: str
    senha: str

@router.post("/registrar")
def registrar(dados: RegistroSchema, db: Session = Depends(get_db)):
    usuario = registrar_usuario(db, dados.nome, dados.email, dados.senha, dados.perfil)
    if not usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    return {"mensagem": "Usuário registrado com sucesso.", "id": usuario.id}

@router.post("/login")
def login(dados: LoginSchema, db: Session = Depends(get_db)):
    resultado = autenticar_usuario(db, dados.email, dados.senha)
    if not resultado:
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")
    return resultado
