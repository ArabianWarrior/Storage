from fastapi import APIRouter
from src.schemas.users import UserRequestAdd
from src.database import async_session_maker
from src.repositories.other_repositories.user import UsersRepositiory


router = APIRouter(prefix="/auth", tags=["Авторазиция и аутентефикация"])


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
    async with async_session_maker() as session:
        user = await UsersRepositiory(session).add(user_data)
        await session.commit()
