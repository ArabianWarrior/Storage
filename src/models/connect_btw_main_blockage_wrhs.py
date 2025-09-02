#связь основного склада и засора
#The connection between the main warehouse and the blockage

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from src.database import Base

class ConnBtwMainBlockageWrhsOrm(Base):
    __tablename__ = "connection btw main and blockage wrhs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    main_warehouse: Mapped[str] = mapped_column(String(100), comment="Склад основной")
    contaminated_warehouse: Mapped[str] = mapped_column(String(100), comment="Склад засор") 