"""Lista visitas comerciais guardadas na base de dados.

Executar com ``python -m app.list_visitas``.
"""

from sqlalchemy import select

from app.db import SessionLocal
from app.models import Visita


def listar_visitas() -> list[Visita]:
    """Devolve as visitas da mais recente para a mais antiga."""
    with SessionLocal() as session:
        return list(
            session.scalars(
                select(Visita).order_by(Visita.realizada_em.desc(), Visita.id.desc())
            )
        )


def main() -> None:
    visitas = listar_visitas()
    if not visitas:
        print("Não existem visitas registadas.")
        return

    for visita in visitas:
        data = visita.realizada_em.strftime("%Y-%m-%d %H:%M %Z")
        notas = visita.notas or "Sem notas"
        print(f"#{visita.id} | {data} | {visita.cliente} | {notas}")


if __name__ == "__main__":
    main()
