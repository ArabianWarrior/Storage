from fastapi import APIRouter
from passlib.context import CryptContext
from src.database import async_session_maker

from src.schemas.users import UserRequestAdd, UserAdd
from src.repositories.other_repositories.user import UsersRepositiory



router = APIRouter(prefix="/auth", tags=["Авторазиция и аутентефикация"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
