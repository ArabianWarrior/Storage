from pydantic import BaseModel, ConfigDict

class UserAdd(BaseModel):
    email: str
    nickname: str
    hashed_password: str

class UserUpdate(BaseModel):
    email: str | None = None
    nickname: str | None = None

class UserUpdatePass(BaseModel):
    old_password: str 
    new_password: str 

class UserCreate(BaseModel):
    email: str
    nickname: str
    password: str

class User(BaseModel):
    id: int
    email: str
 
    model_config = ConfigDict(from_attributes=True)


#Опциональные параметры - объяснение
#Это поля которые могут быть переданы или не переданы в запросе
#Пример использования:
# Обновить только email {"email": new@mail.com}
#Обновить только nickname {"nickname": "John Johns"}
#Или мы хотим обновить сразу два поля
# {"email": new@mail.com}, {"nickname": "John Johns"}

#Где применяются:
# PATCH запросы - частичное обновление:
# Обновление профиля пользователя
# Изменение настроек
# Обновление статуса заказа

# Фильтрация в GET запросах:
# Поиск товаров по цене ИЛИ категории ИЛИ обоим параметрам

# Настройки по умолчанию:
# Создание записей с опциональными параметрами