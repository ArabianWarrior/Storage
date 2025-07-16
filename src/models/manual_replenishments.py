#Ручное пополнение расчетных счетов
#Manual replenishment of current accounts

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  Boolean, Date, Integer, Numeric, String, Time


class ManualRepleOrm(Base):
    __tablename__ = "manual replenishment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)  
    replenishment_number: Mapped[str] = mapped_column(String(50), comment="Номер пополнения")  
    account_number: Mapped[str] = mapped_column(String(50), comment="Расчетный счет")  
    creation_date: Mapped[Date] = mapped_column(Date, comment="Дата создания")  
    creation_time: Mapped[Time] = mapped_column(Time, comment="Время создания")  
    created_by: Mapped[str] = mapped_column(String(100), comment="Создал")  
    amount: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Сумма") 
    delete_indicator: Mapped[Boolean] = mapped_column(Boolean, default=False, comment="Индикатор удаления") 