from decimal import Decimal
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Float, String, Numeric

class ActPositionsOrm(Base):
    __tablename__ = "act_positions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    act_number: Mapped[str] = mapped_column(String(50), comment="Номер акта")
    position_number: Mapped[int] = mapped_column(Integer, comment="Номер позиции")
    material: Mapped[str] = mapped_column(String(100), comment="Материал")
    gross_weight_kg: Mapped[float] = mapped_column(Float, comment="Вес брутто (кг)")
    fact_price_per_kg: Mapped[Decimal] = mapped_column(Numeric(10, 2), comment="Цена за факт (за кг)")
    plan_price_per_kg: Mapped[Decimal] = mapped_column(Numeric(10, 2), comment="Цена за план (за кг)")
    contamination_percent: Mapped[float] = mapped_column(Float, comment="Засор (%)")
    contamination_kg: Mapped[float] = mapped_column(Float, comment="Засор (кг)")
    net_weight_kg: Mapped[float] = mapped_column(Float, comment="Вес нетто (кг)")
    planned_cost: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Стоимость (план)")
    actual_cost: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Стоимость (факт)")
