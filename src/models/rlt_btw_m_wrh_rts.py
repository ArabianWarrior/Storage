#связь основного склада и возврата
#The relationship between the main warehouse and the return

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from src.database import Base

class RelationshipMainReturnOrm(Base):
    __tablename__ = "relationship btw main and return wrhs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    main_warehouse: Mapped[str] = mapped_column(String(100), comment="Склад основной")
    return_warehouse: Mapped[str] = mapped_column(String(100), comment="Склад возврата")