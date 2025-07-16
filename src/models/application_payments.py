#Приложения по оплате актов приема
#Applications for payment of acceptance certificates

from datetime import date, datetime, time
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, Float, Integer, String, DateTime, Boolean, Time


class ApplicationsPaymentOrm(Base):
    __tablename__ = "application for payment of acceptance certificates"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    application_number: Mapped[str] = mapped_column(String(50), comment="Номер приложения")
    act_number: Mapped[str] = mapped_column(String(50), comment="Номер акта")
    created_date: Mapped[date] = mapped_column(Date, default=datetime.now, comment="Дата создания")
    created_time: Mapped[time] = mapped_column(Time, default=datetime.now, comment="Время создания")
    created_by: Mapped[str] = mapped_column(String(100), comment="Создал")
    issued_amount: Mapped[float] = mapped_column(Float, comment="Выданная сумма (руб)")
    payment_method: Mapped[str] = mapped_column(String(50), comment="Способ оплаты")
    payment_source: Mapped[str] = mapped_column(String(100), comment="Источник оплаты")
    remaining_balance: Mapped[float] = mapped_column(Float, comment="Остаток на момент выдачи суммы")
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, comment="Индикатор удаления")
    deleted_date: Mapped[date] = mapped_column(Date, nullable=True, comment="Дата удаления")
    deleted_time: Mapped[time] = mapped_column(Time, nullable=True, comment="Время удаления")
    deleted_by: Mapped[str] = mapped_column(String(100), nullable=True, comment="Удалил")