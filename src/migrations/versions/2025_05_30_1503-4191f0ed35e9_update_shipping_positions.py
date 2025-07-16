"""update shipping positions

Revision ID: 4191f0ed35e9
Revises: a398374e9fd4
Create Date: 2025-05-30 15:03:58.946670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4191f0ed35e9'
down_revision: Union[str, None] = 'a398374e9fd4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
