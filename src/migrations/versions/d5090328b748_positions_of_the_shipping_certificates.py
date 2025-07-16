"""positions of the shipping certificates

Revision ID: d5090328b748
Revises: a8ac1bdf0a44
Create Date: 2025-04-21 19:19:28.043804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd5090328b748'
down_revision: Union[str, None] = 'a8ac1bdf0a44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Переименование таблицы (если старая существует)
    op.rename_table('positiobs of the shipping certificates', 'positions of the shipping certificates')
    
    # Изменение столбцов
    op.alter_column('positions of the shipping certificates', 'act_number',
                    existing_type=sa.String(length=50),
                    type_=sa.String(length=50),
                    comment='Номер акта')
    
    # Добавьте здесь другие изменения, которые вы сделали в модели
    # Например, если вы изменили типы данных или добавили новые столбцы


def downgrade() -> None:
    # Возврат изменений
    op.rename_table('positions of the shipping certificates', 'positiobs of the shipping certificates')