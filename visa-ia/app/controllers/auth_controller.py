from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.auth.jwt_handler import hash_senha, verificar_senha, criar_token

def registrar_usuario(db: Session, nome: str, email: str, senha: str, perfil: str = "empresa"):
    usuario_existente = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario_existente:
        return None

    usuario = Usuario(
        nome=nome,
        email=email,
        senha=hash_senha(senha),
        perfil=perfil
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def autenticar_usuario(db: Session, email: str, senha: str):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario or not verificar_senha(senha, usuario.senha):
        return None

    token = criar_token({"sub": usuario.email, "perfil": usuario.perfil})
    return {"access_token": token, "token_type": "bearer"}
