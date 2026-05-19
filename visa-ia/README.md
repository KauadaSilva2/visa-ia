# 🏥 VISA IA — Vigilância Sanitária com Inteligência Artificial

Sistema de análise documental automatizada para a Vigilância Sanitária, utilizando OCR, Inteligência Artificial e boas práticas de engenharia de software.

> Projeto de Extensão — Londrina, 2026  
> Integrantes: Erik Victorino · Kauã da Silva Santos · Mateus Gomes

---

## 📌 Objetivo

Automatizar o processo de licenciamento sanitário, reduzindo o tempo de análise documental, minimizando erros humanos e aumentando a escalabilidade do serviço através do uso de OCR e IA.

---

## 🚀 Tecnologias

| Camada         | Tecnologia         | Justificativa                          |
|----------------|--------------------|----------------------------------------|
| Backend        | FastAPI (Python)   | Alta performance e integração com IA   |
| Frontend       | React + Tailwind   | Componentização e flexibilidade        |
| Banco de Dados | PostgreSQL         | Segurança e confiabilidade             |
| OCR            | Tesseract          | Gratuito e open-source                 |
| ORM            | SQLAlchemy         | Organização e segurança                |
| Autenticação   | JWT + bcrypt       | Escalabilidade e segurança             |
| Containers     | Docker Compose     | Facilidade de deploy                   |

---

## 🗂️ Arquitetura

O projeto adota **Clean Architecture** combinada com **MVC**:

```
visa-ia/
│
├── app/
│   ├── controllers/     # Lógica de controle (MVC - Controller)
│   ├── models/          # Entidades do banco (MVC - Model)
│   ├── services/        # Serviços de OCR e IA
│   ├── routes/          # Rotas da API (MVC - View/Router)
│   ├── database/        # Conexão e sessão com o banco
│   └── auth/            # JWT e hashing de senhas
│
├── domain/              # Entidades e regras de negócio (Clean Architecture)
├── use_cases/           # Casos de uso
├── adapters/            # Comunicação entre camadas
├── frameworks/          # FastAPI, banco e libs externas
├── tests/               # Testes unitários e de integração
├── uploads/             # Arquivos enviados pelas empresas
│
├── main.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── .env.example
```

---

## ⚙️ Como Rodar

### Pré-requisitos
- Python 3.11+
- Docker e Docker Compose (opcional)
- Tesseract OCR instalado

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/visa-ia.git
cd visa-ia
```

### 2. Configurar variáveis de ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar a API
```bash
uvicorn main:app --reload
```

### 5. Rodar com Docker
```bash
docker-compose up --build
```

A API estará disponível em: `http://localhost:8000`  
Documentação automática: `http://localhost:8000/docs`

---

## 🔐 Segurança

- Autenticação via **JWT**
- Senhas com **hash bcrypt**
- Controle de acesso por perfil (**RBAC**)
- Conformidade com **LGPD**
- Medidas contra vulnerabilidades **OWASP Top 10**
- Logs de auditoria de todas as ações

---

## 👥 Perfis de Acesso

| Perfil        | Permissões                        |
|---------------|-----------------------------------|
| Empresa       | Upload e consulta de documentos   |
| Analista VISA | Revisão, aprovação e relatórios   |
| Administrador | Controle total do sistema         |

---

## 📡 Endpoints Principais

| Método | Rota                          | Descrição                    |
|--------|-------------------------------|------------------------------|
| GET    | `/`                           | Status da API                |
| POST   | `/auth/registrar`             | Registrar novo usuário       |
| POST   | `/auth/login`                 | Autenticar e obter token     |
| POST   | `/documentos/upload`          | Upload e análise de documento|
| GET    | `/documentos/`                | Listar documentos            |
| PATCH  | `/documentos/{id}/aprovar`    | Aprovar documento            |
| PATCH  | `/documentos/{id}/reprovar`   | Reprovar documento           |

---

## 📚 Referências

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [React](https://react.dev/)
- [OWASP](https://owasp.org/)
- [LGPD](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
