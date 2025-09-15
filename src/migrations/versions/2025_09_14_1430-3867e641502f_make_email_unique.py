"""make email unique

Revision ID: 3867e641502f
Revises: 091666a453c0
Create Date: 2025-09-14 14:30:07.139199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3867e641502f'
down_revision: Union[str, None] = '091666a453c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
