from fastapi import APIRouter, HTTPException
from src.database import async_session_maker
from src.repositories.other_repositories.transfers_of_materials_btw_whs import TransfersMaterialsBtwWhsRepository
from src.models.transfers_of_materials_btw_whs import TransfersMaterialsBtwWhsOrm



router = APIRouter(prefix="/material-transfers", tags=["Material Transfers"])

# GET /{id} - получить перевод по ID
# POST / - создать новый перевод
# GET / - список переводов (без сложных фильтров, как договорились)

# GET /{id} - получить перевод по ID
#Создаем роутер где будем получать конкретный перевод
@router.get("/{material_id}")
#Создаем асинхронную функцию куда передадим наш ID
async def get_one_transfer(material_id: int):
    #Открываем ссесию с базой данных 
    async with async_session_maker() as session:
        #Создаем репозиторий для работы с переводами
        repo = TransfersMaterialsBtwWhsRepository(TransfersMaterialsBtwWhsOrm, session)
        #Ищем наш перевод по id
        transfer = await repo.get_by_id(material_id)
        #Если перевода нет
        if not transfer:
            #Выкинем нашу ошибку
            raise HTTPException(status_code=404, detail="")
        #Возвращаем найденное пополнение
        return transfer

# POST / - создать новый перевод
@router.post("")
async def create_transfer(transfer_data: )



