"""Renaming column from name to full name

Revision ID: c4aff1f96716
Revises: 84a32984b705
Create Date: 2022-09-19 09:09:37.391528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4aff1f96716'
down_revision = '84a32984b705'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'student_name', new_column_name='student_full_name')


def downgrade() -> None:
    op.alter_column('scholars', 'student_full_name', new_column_name='student_name')
