#Акты приема
#Acceptance_certificates

from decimal import Decimal
from datetime import date, datetime, time
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Date, String, DateTime, Boolean, Numeric, Time
from src.database import Base

class AcceptanceCertificatesOrm(Base):
    __tablename__ = "accaptance_certificates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    act_number: Mapped[str] = mapped_column(String(50), comment="Номер акта")
    date_creation: Mapped[date] = mapped_column(Date, comment="Дата создания акта")
    creation_time: Mapped[time] = mapped_column(Time, comment="Время создания акта")
    date_admission: Mapped[datetime] = mapped_column(DateTime, comment="Дата поступления")
    counterparty_name: Mapped[str] = mapped_column(String(100), comment="Наименование контрагента")
    storage: Mapped[str] = mapped_column(String(50), comment="Склад")
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, comment="Дата и время создания записи")
    status: Mapped[str] = mapped_column(String(20), comment="Статус акта")
    reason_rejection: Mapped[str] = mapped_column(String(200), nullable=True, comment="Причина отклонения")
    deletion_indicator: Mapped[bool] = mapped_column(Boolean, default=False, comment="Признак удаления")
    amount_according_act_plan: Mapped[Decimal] = mapped_column(Numeric(10, 2), comment="Сумма по акту (план)")
    amount_according_act_fact: Mapped[Decimal] = mapped_column(Numeric(10, 2), comment="Сумма по акту (факт)")
    extinguished_fact: Mapped[bool] = mapped_column(Boolean, default=False, comment="Факт погашения")
    remainder_fact: Mapped[Decimal] = mapped_column(Numeric(10, 2), comment="Остаток (факт)")
    payment_method: Mapped[str] = mapped_column(String(20), comment="Способ оплаты")