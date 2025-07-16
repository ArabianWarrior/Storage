#Тексты причин отклонения актов отгрузки
#Texts of the reasons for rejecting shipping certificates


from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  Date, Integer, String, Time

class TextsReasonsRejectingShipCrfOrm(Base):
    __tablename__ = "texts of the reasons for rejecting shipping certificates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    act_number: Mapped[str] = mapped_column(String(50), comment="Номер акта")
    rejection_reason_text: Mapped[str] = mapped_column(String(255), comment="Текст причин отклонения")
    created_by: Mapped[str] = mapped_column(String(100), comment="Создал")
    creation_date: Mapped[Date] = mapped_column(Date, comment="Дата создания")
    creation_time: Mapped[Time] = mapped_column(Time, comment="Время создания")