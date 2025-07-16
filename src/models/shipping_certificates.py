#Акты отгрузки
#Shipping certificates
from datetime import date, datetime, time
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Date, Float, Integer, String, DateTime, Time


class ShippingCertificatesOrm(Base):
    __tablename__ = "shipping certificates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    act_number: Mapped[str] = mapped_column(String(50), comment="Номер акта")
    creation_date: Mapped[date] = mapped_column(Date, default=datetime.utcnow, comment="Дата создания")
    creation_time: Mapped[time] = mapped_column(Time, default=datetime.utcnow, comment="Время создания")
    shipment_date: Mapped[DateTime] = mapped_column(DateTime, comment="Дата отгрузки")
    counterparty: Mapped[str] = mapped_column(String(100), comment="Контрагент")
    warehouse: Mapped[str] = mapped_column(String(100), comment="Склад")
    created_by: Mapped[str] = mapped_column(String(100), comment="Создал")
    status: Mapped[str] = mapped_column(String(50), comment="Статус")
    rejection_reason: Mapped[str] = mapped_column(String(200), comment="Причина отклонения (индикатор)")
    vehicle_number: Mapped[str] = mapped_column(String(50), comment="Номер автомобиля")
    deletion_indicator: Mapped[bool] = mapped_column(Boolean, default=False, comment="Индикатор удаления")
    planned_sum: Mapped[float] = mapped_column(Float, comment="Сумма по акту (план)")
    actual_sum: Mapped[float] = mapped_column(Float, comment="Сумма по акту (факт)")
    actual_balance: Mapped[float] = mapped_column(Float, comment="Остаток (факт)")
    paid_status: Mapped[bool] = mapped_column(Boolean, default=False, comment="Погасили (факт)")
