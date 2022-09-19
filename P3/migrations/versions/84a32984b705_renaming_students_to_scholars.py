"""Renaming students to scholars

Revision ID: 84a32984b705
Revises: 361dae855898
Create Date: 2022-09-15 10:57:20.825305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84a32984b705'
down_revision = '361dae855898'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
