#История изменения актуальных цен приема
#History of changes in current admission prices
#caps - current admission prices
from datetime import datetime
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, Integer, String, DateTime

class HistoryChangeCapOrm(Base):
    __tablename__ = "history of changes in caps"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    material: Mapped[str] = mapped_column(String(100), comment="Наименование материала")
    current_price_cash: Mapped[float] = mapped_column(Float, comment="Актуальная цена (наличный расчет)")
    current_price_cashless: Mapped[float] = mapped_column(Float, comment="Актуальная цена (безналичный расчет)")
    entered_by: Mapped[str] = mapped_column(String(100), comment="Кто ввел данные")
    entry_date: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow, comment="Дата ввода")