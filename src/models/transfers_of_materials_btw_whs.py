#переводы материалов между складами
#transfers of materials between warehouses

from datetime import datetime
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, Integer, String, DateTime

class TransfersMaterialsBtwWhsOrm(Base):
    __tablename__ = "transfers of materials between warehouses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    transfer_number: Mapped[str] = mapped_column(String(50), comment="Номер перевода")
    transfer_date: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow, comment="Дата перевода")
    transfer_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow, comment="Время перевода")
    executed_by: Mapped[str] = mapped_column(String(100), comment="Кто выполнил перевод")
    from_warehouse: Mapped[str] = mapped_column(String(100), comment="Из склада")
    to_warehouse: Mapped[str] = mapped_column(String(100), comment="В склад")
    from_material: Mapped[str] = mapped_column(String(100), comment="Из материала")
    to_material: Mapped[str] = mapped_column(String(100), comment="В материал")
    quantity_kg: Mapped[float] = mapped_column(Float, comment="Количество (кг)")
    material_cost: Mapped[float] = mapped_column(Float, comment="Стоимость переводимого материала")
    planned_material_cost: Mapped[float] = mapped_column(Float, comment="Стоимость итогового материала по плану")