#Авторизация и аутентефикация

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100))
    nickname: Mapped[str] = mapped_column(String(100))
    hashed_password: Mapped[str] = mapped_column(String(100))
    