"""make email unique

Revision ID: 091666a453c0
Revises: 4191f0ed35e9
Create Date: 2025-09-14 14:29:15.892912

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '091666a453c0'
down_revision: Union[str, None] = '4191f0ed35e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
