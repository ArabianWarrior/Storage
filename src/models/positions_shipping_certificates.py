#позиции актов отгрузки
#The positions of the shipping certificates


from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  Float, Integer, Numeric, String

class PositionsShippingCertificatesOrm(Base):
    __tablename__ = "positions of the shipping certificates"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    act_number: Mapped[str] = mapped_column(String(50), comment="Номер акта")
    position_number: Mapped[int] = mapped_column(Integer, comment="Номер позиции")
    material: Mapped[str] = mapped_column(String(100), comment="Материал")
    gross_weight_kg: Mapped[float] = mapped_column(Float, comment="Вес брутто (кг)")
    psa_shipping_price_per_kg: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Цена отгрузки ПСА (за кг)")
    warehouse_shipping_price_per_kg: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Цена отгрузки склад (за кг)")
    contamination_percent: Mapped[float] = mapped_column(Float, comment="Засор (%)")
    contamination_kg: Mapped[float] = mapped_column(Float, comment="Засор (кг)")
    return_kg: Mapped[float] = mapped_column(Float, comment="Возврат (кг)")
    net_weight_kg: Mapped[float] = mapped_column(Float, comment="Вес нетто (кг)")
    warehouse_shipping_cost: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Стоимость отгрузки склада")
    psa_shipping_cost: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Стоимость отгрузки ПСА")