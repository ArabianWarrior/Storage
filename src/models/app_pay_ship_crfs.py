#Приложения по оплате актов отгрузки
#Applications for payment of shipping certificates

from datetime import date, time
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Date, Integer, Numeric, String, Time

class AppPayShipCrfsOrm(Base):
    __tablename__ = "applications payment shippings certificates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    application_number: Mapped[str] = mapped_column(String(50), comment="Номер приложения")
    act_number: Mapped[str] = mapped_column(String(50), comment="Номер акта")
    creation_date: Mapped[date] = mapped_column(Date, comment="Дата создания")
    creation_time: Mapped[time] = mapped_column(Time, comment="Время создания")
    created_by: Mapped[str] = mapped_column(String(100), comment="Создал")
    issued_amount_rub: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Выданная сумма (руб)")
    payment_method: Mapped[str] = mapped_column(String(100), comment="Способ оплаты")
    replenishment_account: Mapped[str] = mapped_column(String(50), comment="Счет пополнения")
    balance_at_receiving: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Остаток на момент получения суммы")
    deletion_indicator: Mapped[bool] = mapped_column(Boolean, default=False, comment="Индикатор удаления")
    deletion_date: Mapped[date] = mapped_column(Date, nullable=True, comment="Дата удаления")
    deletion_time: Mapped[time] = mapped_column(Time, nullable=True, comment="Время удаления")
    deleted_by: Mapped[str] = mapped_column(String(100), nullable=True, comment="Удалил")