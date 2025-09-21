from fastapi import APIRouter, HTTPException, Response

from src.api.dependencies import UserIdDep
from src.services.auth import AuthService
from src.database import async_session_maker
from src.schemas.users import UserRequestAdd, UserAdd
from src.api.dependencies import DBDep


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
    db: DBDep
):
    #Хэшированный пароль
    hashed_password = AuthService().hash_password(user_data.password)
    #Добавляем и передаем наши параметры
    new_user_data = UserAdd(email=user_data.email, hashed_password=hashed_password, nickname=user_data.nickname)
    await db.users.add(new_user_data)
    await db.commit()
    #Вернем сообщение что все ок
    return {"status": "OK"}


@router.post("/login")
async def login_user(
    db: DBDep,
    data: UserRequestAdd,
    response: Response,
):
    # hashed_password = pwd_context.hash(data.password)
    # new_user_data = UserAdd(email=data.email, hashed_password=hashed_password, nickname=data.nickname)
    
        user = await db.users.get_one_or_none(email=data.email)
        user = await db.users.get_user_with_hashed_password(email=data.email)
        if not user:
            raise HTTPException(status_code=401, detail="Пользователь с таким email не зарегистрирован")
        if not AuthService().verify_password(data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Пароль неверный")
        access_token = AuthService().create_access_token({"user_id": user.id})
        response.set_cookie("access_token", access_token)
        return {"access_token": access_token}


@router.post("/logout")
async def logout(
    response: Response):
    
    response.delete_cookie("access_token")
    return {"status": "OK"}


#request - запрос
@router.get("/me")
async def get_me(
    user_id: UserIdDep,
    db: DBDep,
):
    user = await db.users.get_one_or_none(id=usr)