from fastapi import FastAPI
from app.routes.documento_routes import router as documento_router
from app.routes.auth_routes import router as auth_router

app = FastAPI(
    title="VISA IA — Vigilância Sanitária com Inteligência Artificial",
    description="Sistema de análise documental automatizada com OCR e IA.",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(documento_router)

@app.get("/")
def home():
    return {"mensagem": "API Vigilância Sanitária — VISA IA"}
