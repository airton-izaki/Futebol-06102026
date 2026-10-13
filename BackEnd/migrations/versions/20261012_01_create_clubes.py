"""Create clubes table.

Revision ID: 20261012_01
Revises:
Create Date: 2026-10-12
"""
from alembic import op
import sqlalchemy as sa

revision = "20261012_01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "clubes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome_oficial", sa.String(length=100), nullable=False),
        sa.Column("nome", sa.String(length=100), nullable=False),
        sa.Column("sigla", sa.String(length=5), nullable=False),
        sa.Column("gestao", sa.String(length=20), nullable=False),
        sa.Column("fundacao", sa.Date(), nullable=False),
        sa.Column("estado", sa.String(length=50), nullable=False),
        sa.Column("cidade", sa.String(length=100), nullable=False),
        sa.Column("estadio", sa.String(length=100), nullable=True),
        sa.Column("cor_primaria", sa.String(length=30), nullable=False),
        sa.Column("cor_secundaria", sa.String(length=30), nullable=True),
        sa.Column("cor_terciaria", sa.String(length=30), nullable=True),
        sa.Column("website", sa.String(length=2048), nullable=True),
        sa.Column("escudo", sa.String(length=2048), nullable=True),
        sa.Column("observacao", sa.Text(), nullable=True),
        sa.Column("ativo", sa.Boolean(), nullable=False),
        sa.Column("criado_em", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("atualizado_em", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_clubes_id"), "clubes", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_clubes_id"), table_name="clubes")
    op.drop_table("clubes")
