from sqlalchemy.orm import Session
from app.models.documento import Documento
from app.services.ocr_service import extrair_texto, classificar_documento

def salvar_documento(db: Session, nome: str, conteudo: bytes, usuario_id: int) -> Documento:
    texto = extrair_texto(conteudo)
    classificacao = classificar_documento(texto)

    doc = Documento(
        nome=nome,
        status="analisado",
        texto_extraido=texto,
        classificacao=classificacao,
        usuario_id=usuario_id
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def listar_documentos(db: Session):
    return db.query(Documento).all()

def aprovar_documento(db: Session, documento_id: int) -> Documento:
    doc = db.query(Documento).filter(Documento.id == documento_id).first()
    if doc:
        doc.status = "aprovado"
        db.commit()
        db.refresh(doc)
    return doc

def reprovar_documento(db: Session, documento_id: int) -> Documento:
    doc = db.query(Documento).filter(Documento.id == documento_id).first()
    if doc:
        doc.status = "reprovado"
        db.commit()
        db.refresh(doc)
    return doc
