"""add users

Revision ID: 8d025da417be
Revises: 00b0c1067639
Create Date: 2025-05-06 14:51:52.531225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d025da417be'
down_revision: Union[str, None] = '00b0c1067639'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nickname', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
)

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    