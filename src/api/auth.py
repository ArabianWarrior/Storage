from datetime import datetime, timedelta, timezone
from fastapi import APIRouter
import jwt
from passlib.context import CryptContext
from src.database import async_session_maker

from src.schemas.users import UserRequestAdd, UserAdd
from src.repositories.other_repositories.user import UsersRepositiory



router = APIRouter(prefix="/auth", tags=["Авторазиция и аутентефикация"])


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#Функция создает access token
#Мы принимает словарь данных
def create_access_token(data: dict) -> str:
    #Создаем переменную и копируем словарик, чтобы не видоизменять его,
    #Потому что словарик это видоизменяемая структура данных
    to_encode = data.copy()
    #Мы создаем переменную и мы хотим понять, 
    # когда заканчивается валидность этого токена(то есть его время)
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #Обновляем время
    to_encode |= ({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/login")
async def login_user(
    user_data: UserRequestAdd,    
):
    # hashed_password = pwd_context.hash(user_data.password)
    # new_user_data = UserAdd(email=user_data.email, hashed_password=hashed_password)
    async with async_session_maker() as session:
        user = await UsersRepositiory(session).get(new_user_data)
        await session.commit()
    return {"status": "OK"}






#Когда мы добавляем какие-либо данные или когда мы используем
#Передачу чувствительных данных по типу: паролей, API ключей, банковских карт
#Мы всегда используем post запрос

#Создаем ручку для регистрации
@router.post("/register")
#Создаем асинхонную функцию куда передадим наши параметры
#Эта функция будет принимать Pydantic схему
async def register_user(
    user_data: UserRequestAdd,    
):
    #Хэшированный пароль
    hashed_password = pwd_context.hash(user_data.password)
    #Добавляем и передаем наши параметры
    new_user_data = UserAdd(email=user_data.email, hashed_password=hashed_password)
    #Открываем сессию c базой данных
    async with async_session_maker() as session:
        #Добавляем нашего пользователя
        user = await UsersRepositiory(session).add(new_user_data)
        #Говорим что сохраним это окончательно
        await session.commit()
    #Вернем сообщение что все ок
    return {"status": "OK"}
