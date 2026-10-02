"""Insere visitas de exemplo na base de dados.

Executar com ``python -m app.seed`` depois de aplicar as migrações.
"""

from datetime import datetime, timezone

from sqlalchemy import select

from app.db import SessionLocal
from app.models import Visita


SEED_VISITAS = (
    {
        "cliente": "Mercearia do Bairro",
        "notas": "Apresentação do catálogo e levantamento das necessidades.",
        "realizada_em": datetime(2026, 9, 15, 10, 0, tzinfo=timezone.utc),
    },
    {
        "cliente": "Café Central",
        "notas": "Seguimento da proposta de fornecimento. Cliente pediu revisão dos preços.",
        "realizada_em": datetime(2026, 9, 18, 14, 30, tzinfo=timezone.utc),
    },
    {
        "cliente": "Oficina Horizonte",
        "notas": "Primeira visita. Agendar demonstração de produto.",
        "realizada_em": datetime(2026, 9, 22, 9, 15, tzinfo=timezone.utc),
    },
)


def seed() -> int:
    """Adiciona registos de exemplo em falta e devolve o número inserido."""
    inserted = 0
    with SessionLocal.begin() as session:
        for dados in SEED_VISITAS:
            existing = session.scalar(
                select(Visita.id).where(
                    Visita.cliente == dados["cliente"],
                    Visita.realizada_em == dados["realizada_em"],
                )
            )
            if existing is None:
                session.add(Visita(**dados))
                inserted += 1
    return inserted


if __name__ == "__main__":
    count = seed()
    print(f"Seed concluído: {count} visita(s) inserida(s).")
