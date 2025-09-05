from fastapi import FastAPI, APIRouter
from src.schemas.positions_shipping_certificates import PositionsShippingCertificatesCreate, PositionsShippingCertificatesUpdate
#позиции актов отгрузки
#The positions of the shipping certificates

router = APIRouter(prefix="/shipping-positions", tags=["Shipping Positions"])

#Get - получить
#Получить позиции актов отгрузки
#Создаем роутер где будем получать позиции актов отгрузки
@router.get("/{position_id}")
#Создаем асинхронную функцию где передадим 1 параметр ( id)
async def get_shipping_position(position_id: int):
    #Выведем сообщение об том что мы получили позиции актов отгрузки
    return {"message": f"Get a shipping position: {position_id}"}

#Post - для добавления
#Создаем роутер где будем добавлять позииции актов отгрузки
@router.post("")
#Создаем асинхронную функцию куда передадим нашу схему
async def create_shipping_position(position_data: PositionsShippingCertificatesCreate):
    #Выведем сообщение об успешном добавлении
    return {"message": "We successfully created a shipping position",
            "data": position_data.model_dump()}

#Delete - для удаления данных
#Создаем ручку где будем удалять данные
@router.delete("/{position_id}")
#Создаем асинхронную функцию куда передадим 1 параметр (id)
async def delete_shipping_position(position_id: int):
    #Выведем сообщение об успешном удалении
    return {"message": f"We successfully deleted a shipping position with ID: {position_id}"}

#Put - для обновления данных
#Создаем ручку где будем обновлять данные
@router.put("/{position_id}")
#Создаем асинхронную функцию куда передадим 2 параметра, 1.id, 2.схема данных
async def update_shipping_position(position_id: int, position_data: PositionsShippingCertificatesUpdate):
    #Выведем сообщение об успешном обновлении данных
    #exclude_unset=True - показывает только те поля, которые клиент действительно хотел изменить
    #исключает все None значения (поля которые не были переданы в запросе)
    return {"message": f"Shipping certificate {position_id} successfully updated",
            "updated_data": position_data.model_dump(exclude_unset=True)}
