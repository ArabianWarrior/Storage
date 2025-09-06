from fastapi import APIRouter, HTTPException
from src.repositories.base import BaseRepository
from src.schemas.manual_replenishments import ManualRepleCreate


#Ручное пополнение расчетных счетов
#Manual replenishment of current accou

router = APIRouter(prefix="/replenishments", tags=["Manual Replenishments"])


#GET /{replenishment_id}    # Получить конкретное пополнение
#POST /                     # Создать пополнение
#DELETE /{replenishment_id} # Отменить пополнение (soft delete)

#Создаем ручку где получаем конкретное пополнение
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

    #Возвращаем найденное пополенение
    return replenishment

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