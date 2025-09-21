from fastapi import APIRouter, HTTPException
from src.schemas.application_payments import ApplicationPaymentsCreate, ApplicationPaymentsUpdate
from src.api.dependencies import DBDep


#Приложения по оплате актов приема
#Applications for payment of acceptance certificates

router = APIRouter(prefix="/applications", tags=["Applications"])


#Создаем ручку для получения конкретного платежа по его ID
@router.get("/{application_id}") 
#payment_id - уникальный идентификатор платежа в базе данных
#Нужен для поиска конкретного платежа среди множества записей
#Например: GET /payments/123 вернет платеж с ID=123
#Без ID невозможно понять какой именно платеж нужен пользователю
async def get_application(application_id: int):
    #Выводим сообщение об нашем платеже
    return {"message": f"You get a payment application: {application_id}"}
#Примеры использования:
# Обновить примеры:
#Например: GET /applications/123 вернет заявку с ID=123
# GET /applications/1 - заявка №1


#Создаем ручку где будет создан запрос на платеж
@router.post("")
#Создаем асинхронную функцию где будет передан наш параметр
async def create_application(application_data: ApplicationPaymentsCreate):
    #Выведем наше сообщение об успешном создании заявки на платеж
    return {"message": "You have successfully created a payment request",
            "data": application_data.model_dump()}


#Здесь мы используем метод из нашего базового репозитория
#Создаем ручку для мягкого удаления заявки на платеж
@router.delete("/{application_id}")
#application_id - ID заявки из URL, application_repo - репозиторий через Depends
async def soft_delete_application(
    application_id: int, 
    db: DBDep,
):
    #Вызываем метод мягкого удаления из базового репозитория
    deleted_payment = await db.application.soft_delete(application_id, "is_deleted")
    
    #Если заявка не найдена - выбрасываем ошибку 404
    if not deleted_payment:
        raise HTTPException(status_code=404, detail="Payment application not found")
    
    #Возвращаем сообщение об успешном удалении
    return {
        "message": f"Payment application {application_id} successfully deleted",
        "deleted_application": deleted_payment
    }

#Создаем ручку где будет обновлять данные об нашем заявке
#Здесь будет передан определенный стек параметров которые можно изменять
@router.put("/{application_id}")
#Создаем асинхронную функцию, где будет передано 3 параметра
async def update_payment_application(
    application_id: int, 
    db: DBDep,
    application_data: ApplicationPaymentsUpdate
    ):
    #Создаем значение где будет происходить обновление
    update_with_id = await db.application.update_by_id(
        application_id, #ID записи которую обновляем (например: 123)
        application_data.model_dump(exclude_unset=True) #Данные для обновления
        )

    #Если обновление не произошло
    if not update_with_id:
        #Выведем нашу ошибку
        raise HTTPException(status_code=404, detail="Payments update not found")
    #Выведем сообщение об обновлении
    return {
        "message": f"Payment application {application_id} successfully updated",
        "updated_application": application_data.model_dump(exclude_unset=True)
    }
    #exclude_unset=True - показывает только те поля, которые клиент действительно хотел изменить
    # исключает все None значения (поля которые не были переданы в запросе)

