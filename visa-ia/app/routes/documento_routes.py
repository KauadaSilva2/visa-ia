from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.controllers.documento_controller import (
    salvar_documento, listar_documentos, aprovar_documento, reprovar_documento
)

router = APIRouter(prefix="/documentos", tags=["Documentos"])

@router.post("/upload")
async def upload_documento(
    file: UploadFile = File(...),
    usuario_id: int = 1,
    db: Session = Depends(get_db)
):
    conteudo = await file.read()
    doc = salvar_documento(db, file.filename, conteudo, usuario_id)
    return {
        "arquivo": doc.nome,
        "status": doc.status,
        "classificacao": doc.classificacao,
        "texto_extraido": doc.texto_extraido[:300] if doc.texto_extraido else ""
    }

@router.get("/")
def listar(db: Session = Depends(get_db)):
    docs = listar_documentos(db)
    return docs

@router.patch("/{documento_id}/aprovar")
def aprovar(documento_id: int, db: Session = Depends(get_db)):
    doc = aprovar_documento(db, documento_id)
    return {"id": doc.id, "status": doc.status}

@router.patch("/{documento_id}/reprovar")
def reprovar(documento_id: int, db: Session = Depends(get_db)):
    doc = reprovar_documento(db, documento_id)
    return {"id": doc.id, "status": doc.status}
