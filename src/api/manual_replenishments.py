from fastapi import APIRouter, HTTPException
from src.repositories.base import BaseRepository
from src.schemas.manual_replenishments import ManualRepleCreate


#Ручное пополнение расчетных счетов
#Manual replenishment of current accou

router = APIRouter(prefix="/replenishments", tags=["Manual Replenishments"])


#GET /{replenishment_id}    # Получить конкретное пополнение
#POST /                     # Создать пополнение
#DELETE /{replenishment_id} # Отменить пополнение (soft delete)

#GET /{replenishment_id}    # Получить конкретное пополнение
#Создаем ручку где получаем конкретное пополнeние
@router.get("/{replenishment_id}")
#Создаем асинхронную функцию, куда будет передано два параметра
async def get_replenishment(replenishment_id: int, repo: BaseRepository):
    #Получаем пополнение из базы данных
    replenishment = await repo.get_by_id(replenishment_id)

    #Если пополнение не найдено
    if not replenishment:
        raise HTTPException(status_code=404, detail="Replenishment not found")  
    
    # Проверяем не удалено ли пополнение
    if replenishment.delete_indicator:
        raise HTTPException(status_code=404, detail="Replenishment was deleted")

    #Возвращаем найденное пополнение
    return replenishment

#POST / # Создать пополнение
#Создаем ручку, где будет создаваться пополнение
@router.post("")
#Создаем асинхронную функцию где будут переданы 3 параметра
async def create_replenishment(
    replenishment_data: ManualRepleCreate, 
    repo: BaseRepository,
    ):
    
    # 1. Добавить await и model_dump()
    replenishment = await repo.create(replenishment_data.model_dump())

    # 2. Проверить что создание прошло успешно
    if not replenishment:
        raise HTTPException(status_code=400, detail="Failed to create replenishment")
    
    # 3. Вернуть результат
    return {
        "message": "Replenishment successfully created",
        "data": replenishment }


#DELETE /{replenishment_id} # Отменить пополнение (soft delete)
#Создаем ручку где будем отменять пополнение с помощью soft_delete
@router.delete("/{replenishment_id}")
#Создаем асинхронную функцию где передадим 2 параметра
async def replenishment_soft_delete(replenishment_id: int, repo: BaseRepository):
    #Создадим значение где будет наш функционал
    deleted_replenishment = await repo.soft_delete(replenishment_id, "delete_indicator")

    #Если не удалилось
    if not deleted_replenishment:
        #То мы выведем ошибку
        raise HTTPException(status_code=404, detail="Replenishment not found")
    
    #Выведем сообщение об удалении
    return {
        "message": f"Manual replenishment {replenishment_id} successfully deleted",
        "deleted_replenishment": deleted_replenishment
    }