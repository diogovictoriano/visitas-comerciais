"""Configuração de ligação e sessões da base de dados."""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://visitas:altere-esta-senha@localhost:5432/visitas",
)


class Base(DeclarativeBase):
    """Classe base dos modelos SQLAlchemy."""


engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
