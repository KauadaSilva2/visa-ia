from sqlalchemy import Column, Integer, String, Enum
from app.database.connection import Base
import enum

class PerfilEnum(str, enum.Enum):
    empresa = "empresa"
    analista = "analista"
    administrador = "administrador"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    perfil = Column(Enum(PerfilEnum), default=PerfilEnum.empresa)
