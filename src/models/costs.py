#Расходы

from datetime import date, datetime, time
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Date, Integer, Numeric, String, Time
from src.database import Base

class CostrsOrm(Base):
    __tablename__ = "the costs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    expense: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Расход")
    payment_method: Mapped[str] = mapped_column(String(20), comment="Способ оплаты")
    payment_source: Mapped[str] = mapped_column(String(100), comment="Источник оплаты")
    amount_rub: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Сумма руб")
    comment: Mapped[str] = mapped_column(String(255), comment="Комментарий")
    created_date: Mapped[date] = mapped_column(Date, default=date.today, comment="Дата создания")
    created_time: Mapped[time] = mapped_column(Time, default=lambda: datetime.now.time(), comment="Время создания")
    created_by: Mapped[str] = mapped_column(String(100), comment="Создал")
    deletion_indicator: Mapped[bool] = mapped_column(Boolean, default=False, comment="Индикатор удаления")
    deleted_date: Mapped[date] = mapped_column(Date, nullable=True, comment="Дата удаления")
    deleted_time: Mapped[time] = mapped_column(Time, nullable=True, comment="Время удаления")
    deleted_by: Mapped[str] = mapped_column(String(100), nullable=True, comment="Удалил")