from datetime import datetime, timezone, timedelta

from fastapi import HTTPException
import jwt
from passlib.context import CryptContext

from src.config import settings

#В этом файле мы храним весь функционал
#Для работы с авторизацией и аутентефикацией
#Я вынес все эти методы в отдельную файл, чтобы ручки
#В API не были большими, вся логика должна быть вынесена за пределы


class AuthService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    #Проверка пароля
    def verify_password(self, plain_password: str, hashed_password: str) -> str:
        return self.pwd_context.verify(plain_password, hashed_password)
    #Хэшируем пароль
    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)
    
    #Функция создает access token
    #Мы принимает словарь данных
    def create_access_token(self, data: dict) -> str:
        #Создаем переменную и копируем словарик, чтобы не видоизменять его,
        #Потому что словарик это видоизменяемая структура данных
        to_encode = data.copy()
        #Мы создаем переменную и мы хотим понять, 
        # когда заканчивается валидность этого токена(то есть его время)
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        #Обновляем время
        to_encode |= ({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    def decode_token(self, token: str) -> dict:
        try:
            return jwt.decode(token, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        except jwt.exceptions.DecodeError:
            raise HTTPException(status_code=401, detail="Неверный токен")

    
