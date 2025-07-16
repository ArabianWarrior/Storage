#Кассир
#Cashriers

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  Date, Integer, Numeric, String, Time

class CashiersOrm(Base):
    __tablename__ = "the cashiers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)  
    cashier_name: Mapped[str] = mapped_column(String(100), comment="Кассир")  
    cash_balance: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Остаток на кассире") 