#Расчетные счета
#Current accounts


from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Numeric, String

class CurrentAccountsOrm(Base):
    __tablename__ = "current accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    account_number: Mapped[str] = mapped_column(String(50), comment="Расчетный счет")
    balance_on_account: Mapped[Numeric] = mapped_column(Numeric(10, 2), comment="Остаток на расчетный счет")