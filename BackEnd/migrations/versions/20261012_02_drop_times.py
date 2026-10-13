"""Drop the legacy times table.

Revision ID: 20261012_02
Revises: 20261012_01
Create Date: 2026-10-12
"""
from alembic import op
import sqlalchemy as sa

revision = "20261012_02"
down_revision = "20261012_01"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("times")


def downgrade() -> None:
    op.create_table(
        "times",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("estado", sa.String(length=2), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
