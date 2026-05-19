from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensagem" in response.json()

def test_listar_documentos():
    response = client.get("/documentos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
