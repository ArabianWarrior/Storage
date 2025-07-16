#Запасы на складах
#Stocks in warehouses

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Numeric, String

class StocksWarehousesOrm(Base):
    __tablename__ = "stocks in warehouses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    warehouse: Mapped[str] = mapped_column(String(100), comment="Склад")
    material: Mapped[str] = mapped_column(String(100), comment="Материал")
    quantity_kg: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Количество (кг)")
    actual_cost: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Стоимость (факт)")
    planned_cost: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Стоимость (план)")