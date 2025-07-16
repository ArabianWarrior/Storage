#Актуальные цены приема
#Current admission prices

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, Integer, String

class CurrentAdmissionPricesOrm(Base):
    __tablename__ = "current admission prices"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    material: Mapped[str] = mapped_column(String(100), comment="Наименование материала")
    current_price_cash: Mapped[float] = mapped_column(Float, comment="Актуальная цена (наличный расчет)")
    current_price_cashless: Mapped[float] = mapped_column(Float, comment="Актуальная цена (безналичный расчет)")