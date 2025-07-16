from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, DateTime, ForeignKey
from src.database import Base

class ReasonsRejectOrm(Base):
    __tablename__ = "reasons_rejection"  
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    act_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("acceptance_acts.id"),  
        nullable=False,
        comment="ID связанного акта приема"
    )
    reason_text: Mapped[str] = mapped_column(String(500), comment="Текст причины отклонения")
    creator: Mapped[str] = mapped_column(String(100), comment="Идентификатор создателя записи")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, comment="Дата и время создания записи")