import pytesseract
from PIL import Image
import io

def extrair_texto(conteudo: bytes, tipo: str = "image") -> str:
    """
    Extrai texto de imagem via OCR (Tesseract).
    Para PDFs, deve ser convertido antes com pdf2image.
    """
    try:
        imagem = Image.open(io.BytesIO(conteudo))
        texto = pytesseract.image_to_string(imagem, lang="por")
        return texto.strip()
    except Exception as e:
        return f"Erro ao processar OCR: {str(e)}"

def classificar_documento(texto: str) -> str:
    """
    Classificação simples de documento com base em palavras-chave.
    Pode ser substituída por modelo de ML no futuro.
    """
    texto_lower = texto.lower()

    if "cnpj" in texto_lower or "razão social" in texto_lower:
        return "Cadastro Empresarial"
    elif "alvará" in texto_lower or "licença" in texto_lower:
        return "Alvará Sanitário"
    elif "laudo" in texto_lower or "análise" in texto_lower:
        return "Laudo Técnico"
    elif "contrato" in texto_lower:
        return "Contrato"
    else:
        return "Documento Geral"
