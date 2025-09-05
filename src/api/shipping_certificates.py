from fastapi import APIRouter, Body
from src.schemas.shipping_certificates import ShippingCertificatesCreate, ShippingCertificatesUpdate

#Акты отгрузки
#Shipping certificates
router = APIRouter(prefix="/shipping-certificates", tags=["Shipping Certificates"])

#Get - получить
#Получить акты отгрузки
#Создаем роутер в котором будет получать акты отгрузки
@router.get("/{certificate_id}")
#Создаем асинхронную ручку которая будет принимать 1 параметр
async def get_certificates(certificate_id: int):
    #Возвращаем сообщение об том что мы получили акты отгрузки
    return {"message": f"Get a shipping certificate: {certificate_id}"}

#Создаем ручку где будем создавать акт отгрузки. Post
@router.post("")
#Создаем асихронную ручку где будет передана схема 
async def create_certificates(certificates_data: ShippingCertificatesCreate):
    #Выводим сообщение об успешном создании актов отгрузки
    return {
        "message": "We successfully created a shipping certificate",
        "data": certificates_data.model_dump()} #В параметр model_dump передаются все модельки

#Создаем ручку где будем удалять акт отрузки. Delete
@router.delete("/{certificate_id}")
#Создаем асинхронную ручку где будет передан 1 параметр (id)
async def delete_certificates(certificate_id: int):
    #Выводим сообщение об успешном удалении
    return {"message": f"We successfully deleted a shipping certificate with ID: {certificate_id}"}

#Создаем ручку где будем обновления данных. Put 
@router.put("/{certificate_id}")
#Создаем асинхронную ручку где будем обновлять данные
async def update_certificates(certificate_id: int, certificates_data: ShippingCertificatesUpdate):
    #Выводим сообщение об успешном обновлении данных
    #exclude_unset=True - показывает только те поля, которые клиент действительно хотел изменить
    # исключает все None значения (поля которые не были переданы в запросе)
    return {"message": f"Certificate {certificate_id} successfuly updated",
            "updated_data": certificates_data.model_dump(exclude_unset=True)} #Покажет только измененные поля

#Пример для ручки Put
#Входные данные от клиента
# {
#   "status": "Завершен",
#   "actual_sum": 14500.00
# }

#что будет в обьекте certificates_data
#ShippingCertificatesUpdate(
#     status="Завершен",
#     actual_sum=14500.00,
#     act_number=None,          # Не передано
#     creation_date=None,       # Не передано  
#     counterparty=None,        # Не передано
#     # ... все остальные поля = None
# )

#И теперь как будет работать с model_dump(exclude_unset=True)
#{
#     'status': 'Завершен',
#     'actual_sum': Decimal('14500.00')
# }
# # Только реально переданные поля!