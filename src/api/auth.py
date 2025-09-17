from fastapi import APIRouter, HTTPException, Response, Request

from services.auth import AuthService
from src.database import async_session_maker
from src.schemas.users import UserRequestAdd, UserAdd
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
    #Хэшированный пароль
    hashed_password = AuthService().hash_password(user_data.password)
    
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


#Создаем ручку где мы будем логиниться
@router.post("/login")
#Асинхронная функция где пользователь будет логиниться
#Передаем сюда 2 параметра
async def login_user(
    user_data: UserRequestAdd,
    response: Response,
):
    #Открываем ссессию с базой данных
    async with async_session_maker() as session:
       
        #Получаем email пользователя
        user = await UsersRepositiory(session).get_user_with_hashed_password(email=user_data.email)
        
        #Проверяем существует ли пользователь под таким email
        #Если нет
        if not user:
            #То вернем ошибку пользователю
            raise HTTPException(status_code=401, detail="Пользователя с таким email не существует")
        
        #Проверяем совпадает ли пароль пользователь
        #Если нет
        if not AuthService().verify_password(user_data.password, user.hashed_password):
            #То вернем ошибку пользователю
            raise HTTPException(status_code=401, detail="Пароль не верный")
        
        access_token = AuthService().create_access_token({"user_id": user.id})
        
        #Мы отправляем файл в cookie
        #Response помимо того что добавляет еще cookie, помимо того что отправляет ответ
        response.set_cookie("access_token", access_token) 
        
        #Так же мы отправим файл в виде JSON
        return {"access_token": access_token}

#request - запрос
@router.get("/only_auth")
async def only_auth(
    request: Request
):
    access_token = request.cookies.get("access_token", None)
    data = AuthService().decode_token(access_token)
    user_id = data["user_id"]
    async with async_session_maker() as session:
        user = await UsersRepositiory(session).get_one_or_none(id=user_id)
        return user