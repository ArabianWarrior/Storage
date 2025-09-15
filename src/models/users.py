#Авторизация и аутентефикация

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
import jwt

class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    #unique=True, позволяет сделать поле email уникальным,
    #у нас не должно быть двух пользователей с одинаковым email
    email: Mapped[str] = mapped_column(String(100), unique=True)
    nickname: Mapped[str] = mapped_column(String(100))
    hashed_password: Mapped[str] = mapped_column(String(100))
    