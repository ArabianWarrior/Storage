#Движение средств между кассирами
#Movement of funds between cashiers

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  Date, Integer, Numeric, String, Time

class MoveCashiersOrm(Base):
    __tablename__ = "movement cashiers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)  
    transfer_number: Mapped[str] = mapped_column(String(50), comment="Номер перевода") 
    donor_cashier: Mapped[str] = mapped_column(String(100), comment="Кассир донор") 
    recipient_cashier: Mapped[str] = mapped_column(String(100), comment="Кассир рецепиент")  
    creation_date: Mapped[Date] = mapped_column(Date, comment="Дата создания")  
    creation_time: Mapped[Time] = mapped_column(Time, comment="Время создания")  
    performed_by: Mapped[str] = mapped_column(String(100), comment="Выполнил перевод")  
    amount: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Сумма")