"""Cria a tabela de visitas.

Revision ID: 0001_create_visitas
Revises:
Create Date: 2026-10-02
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0001_create_visitas"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "visitas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("cliente", sa.String(length=200), nullable=False),
        sa.Column("notas", sa.String(length=2000), nullable=True),
        sa.Column(
            "realizada_em",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_visitas_cliente", "visitas", ["cliente"])


def downgrade() -> None:
    op.drop_index("ix_visitas_cliente", table_name="visitas")
    op.drop_table("visitas")
