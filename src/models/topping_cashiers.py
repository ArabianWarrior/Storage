#Пополнения счетов кассира
#Topping up cashier's accounts


from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  Boolean, Date, Integer, Numeric, String, Time

class TopCashiersOrm(Base):
    __tablename__ = "toppings up cashiers acc"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    replenishment_number: Mapped[str] = mapped_column(String(50), comment="Номер пополнения")  
    cashier: Mapped[str] = mapped_column(String(100), comment="Кассир") 
    date: Mapped[Date] = mapped_column(Date, comment="Дата")  
    time: Mapped[Time] = mapped_column(Time, comment="Время")  
    created_by: Mapped[str] = mapped_column(String(100), comment="Создал")  
    amount: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Сумма")  
    delete_indicator: Mapped[Boolean] = mapped_column(Boolean, default=False, comment="Индикатор удаления")  