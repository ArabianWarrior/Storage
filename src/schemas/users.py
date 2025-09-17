from pydantic import BaseModel, ConfigDict, EmailStr

class UserRequestAdd(BaseModel):
    email: EmailStr
    nickname: str
    password: str

class UserAdd(BaseModel):
    email: EmailStr
    nickname: str
    hashed_password: str

class User(BaseModel):
    id: int
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class UserWithHashedPass(User):
    hashed_password: str

class UserWithHashedPass(User):
    hashed_password: str



#Для чего нужен model_config 
#Простыми словами
#Без from_attributes=True Pydantic принимает только словари 
#Пример: {"name": "John"}
#С from_attributes=True Pydantic может взять данные из любого обьекта
#у которого есть нужные атрибуты
#Пример: obj.name, obj.email
#Эта настройка говорит: Pydantic, умей читать данные не только из словарей'
#но и из атрибутов обьектов





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