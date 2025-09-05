from fastapi import APIRouter, Body
from src.schemas.users import UserCreate, UserUpdate, UserUpdatePass
from src.repositories.other_repositories.user import UsersRepositiory
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import Field

#Правило для ID параметров в RestAPI
#id нужен когда работаешь с КОНКРЕТНЫМ ресурсом
#Например:
#GET /users/{user_id} - получить конкретного пользователя
#В PUT /users/{user_id} - обновить конкретного пользователя
#ID не нужен когда работаешь с коллекцией
#GET /users - получить всех пользователей


#APIRouter - это группировщик эндпоинтов, он создает группу связанных маршрутов
#которые затем подключаются к основному FastAPI приложению
#он позвоялет задать общий префикс
#Аналогия:
#APIRouter как папка в файловой системе 
# - объединяет связанные файлы (эндпоинты) под одним именем (префиксом).

#Таким образом в нашем файле, будем автоматически задан префикс users, на всех ручках
router = APIRouter(prefix="/users", tags=["Users"])

#Для чего нужен tags:
#Tags как меню ресторана - Первые блюда, Вторые блюда, Десерты и тд
#Помогает поситителям (разработчикам) быстро найти нужную группу эндпоинтов
#Если не указать tags - все эндпоинты будут в одной куче без группировки
#С Tags: Users - GET /users/{user_id}, POST /users/
#Hotels: GET /hotels/{hotel_id}, POST /hotels/
#Без Tags: GET /users/{user_id}, GET /hotels/{hotel_id}, GET /bookings/{booking_id}
#Все будет вместе и не будет никакой группировки


#Get нужен для получения данных
#Создаем ручку в котором будет получать id пользователя
@router.get("/{user_id}") #станет: GET /users/{user_id}
#создаем асинхронную функцию, где будет лежать параметр id
async def get_user(user_id: int):
    #выводим сообщение об получении id пользователя
    return {"message": f"We get a user with this id: {user_id}"}

#Для чего нужен Body указывает что данные должны приходить в HTTP запросе
#а не в URL параметрах
#Иными словами без Body async def create_user(user_data: UserCreate):
#Вывод: /users/?email=test&nickname=john&password=123
#С Body async def create_user(user_data: UserCreate = Body()):
#Вывод: {
#    "email": "test@mail.com",
#    "nickname": "john", 
#    "password": "123"
#}


#Создаем ручку для добававления данных. Post
@router.post("") # станент router.post("/users/"), потому что у нас задан префикс
#Создаем асинхронную функцию, которая принимает параметр: user_data
async def create_user(user_data: UserCreate = Body()):
    #Выводим сообщение о создании пользователя
    return {"message": f"We created a new user:{user_data.email}, {user_data.nickname}"}

#Создаем ручку для обновления данных. Put
@router.put("/{user_id}")
#Асинхронная функция, которая принимает два параметра, id и user_data
async def update_user(user_id: int, user_data: UserUpdate = Body()):
    #Выводим сообщение об обновлении данных
    return {"message": f"We updated a user: {user_data.email}, {user_data.nickname}"}

#DELETE запросы НЕ должны иметь тело запроса. DELETE удаляет ресурс только по ID.
#Логика DELETE:
#Что нужно для удаления: Только ID пользователя
#Что НЕ нужно: Никакие дополнительные данные

#Создаем ручку для удаления данных. Delete
@router.delete("/{user_id}")
#Создаем асинхронную функцию, которая принимает один параметра user_id 
async def delete_user(user_id: int):
    #Выведем сообщение об удалении данных
    return {"message": f"We successfully deleted user with ID: {user_id}"}

#Создаем ручку для изменения данных пароля. Put
@router.put("/{user_id}/password")
#Создаем асинхронную функцию, которая принимает параметр user_data
async def change_password(user_id: int, password_data: UserUpdatePass = Body()):
    #Выведем сообщение об успешное изменении пароля
    return {"message": f"We successfuly updated password: {user_id}"}
