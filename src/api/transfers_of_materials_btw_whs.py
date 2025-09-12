from fastapi import APIRouter, HTTPException
from src.database import async_session_maker
from src.repositories.other_repositories.transfers_of_materials_btw_whs import TransfersMaterialsBtwWhsRepository
from src.models.transfers_of_materials_btw_whs import TransfersMaterialsBtwWhsOrm
from src.schemas.transfers_of_materials_btw_whs import TransfersMaterialsBtwWhsCreate



router = APIRouter(prefix="/material-transfers", tags=["Material Transfers"])

# GET /{id} - получить перевод по ID
# POST / - создать новый перевод
# GET / - список переводов (без сложных фильтров, как договорились)

# GET /{id} - получить перевод по ID
#Создаем роутер где будем получать конкретный перевод
@router.get("/{transfer_id}")
#Создаем асинхронную функцию куда передадим наш ID
async def get_one_transfer(transfer_id: int):
    #Открываем ссесию с базой данных 
    async with async_session_maker() as session:
        #Создаем репозиторий для работы с переводами
        repo = TransfersMaterialsBtwWhsRepository(TransfersMaterialsBtwWhsOrm, session)
        #Ищем наш перевод по id
        transfer = await repo.get_by_id(transfer_id)
        #Если перевода нет
        if not transfer:
            #Выкинем нашу ошибку
            raise HTTPException(status_code=404, detail="Transfer not found")
        #Возвращаем найденное пополнение
        return transfer

# POST / - создать новый перевод
@router.post("")
async def create_transfer(transfer_data: TransfersMaterialsBtwWhsCreate):
    # Открываем ссесию с базой данных (исправил "ссесию" → "сессию")
    async with async_session_maker() as session:
        # Создаем репозиторий для работы с переводами
        repo = TransfersMaterialsBtwWhsRepository(TransfersMaterialsBtwWhsOrm, session)
        # Создаем новый перевод в БД, преобразуя схему в словарь
        transfer = await repo.create(transfer_data.model_dump())
        # Если создание не удалось - возвращаем ошибку 400
        if not transfer:
            raise HTTPException(status_code=400, detail="Failed to create material transfer")
        # Возвращаем сообщение об успехе и созданные данные
        return {"message": "Material transfer created", "data": transfer}


@router.get("")
async def get_all_transfers():
    # Открываем сессию с базой данных
    async with async_session_maker() as session:
        # Создаем репозиторий для работы с переводами
        repo = TransfersMaterialsBtwWhsRepository(TransfersMaterialsBtwWhsOrm, session)
        # Используем готовый метод из BaseRepository
        transfers = await repo.get_all()
        # Возвращаем список всех переводов
        return {"transfers": transfers}