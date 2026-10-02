"""Modelos SQLAlchemy da aplicação."""

from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Visita(Base):
    """Registo simples de uma visita comercial."""

    __tablename__ = "visitas"

    id: Mapped[int] = mapped_column(primary_key=True)
    cliente: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    notas: Mapped[str | None] = mapped_column(String(2000))
    realizada_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
