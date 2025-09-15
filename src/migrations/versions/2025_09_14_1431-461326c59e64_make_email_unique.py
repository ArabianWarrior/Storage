"""make email unique

Revision ID: 461326c59e64
Revises: 3867e641502f
Create Date: 2025-09-14 14:31:49.820450

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "461326c59e64"
down_revision: Union[str, None] = "3867e641502f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
