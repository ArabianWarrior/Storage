"""create act_position

Revision ID: 5ec9f8a27345
Revises: ff7ca2e8e8d2
Create Date: 2025-04-21 17:03:50.332575

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5ec9f8a27345'
down_revision: Union[str, None] = 'ff7ca2e8e8d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Проверяем существование таблицы
    inspector = sa.inspect(op.get_bind())
    if not inspector.has_table('act_positions'):
        op.create_table('act_positions',
            sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
            sa.Column('act_number', sa.String(length=50), nullable=False, comment="Номер акта"),
            sa.Column('position_number', sa.Integer(), nullable=False, comment="Номер позиции"),
            sa.Column('material', sa.String(length=100), nullable=False, comment="Материал"),
            sa.Column('gross_weight_kg', sa.Float(), nullable=False, comment="Вес брутто (кг)"),
            sa.Column('fact_price_per_kg', sa.Numeric(precision=10, scale=2), nullable=False, comment="Цена за факт (за кг)"),
            sa.Column('plan_price_per_kg', sa.Numeric(precision=10, scale=2), nullable=False, comment="Цена за план (за кг)"),
            sa.Column('contamination_percent', sa.Float(), nullable=False, comment="Засор (%)"),
            sa.Column('contamination_kg', sa.Float(), nullable=False, comment="Засор (кг)"),
            sa.Column('net_weight_kg', sa.Float(), nullable=False, comment="Вес нетто (кг)"),
            sa.Column('planned_cost', sa.Numeric(precision=10, scale=2), nullable=False, comment="Стоимость (план)"),
            sa.Column('actual_cost', sa.Numeric(precision=10, scale=2), nullable=False, comment="Стоимость (факт)"),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('act_number', 'position_number', name='uq_act_position')
        )
    else:
        print("Table 'act_positions' already exists")

def downgrade() -> None:
    op.drop_table('act_positions')