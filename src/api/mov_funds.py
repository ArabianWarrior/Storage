from datetime import date
from typing import Optional
from fastapi import APIRouter, HTTPException


from src.schemas.mov_funds import MoveFundsCreate
from src.models.mov_funds import MoveFundsOrm  # модель
from src.repositories.other_repositories.mov_funds import MoveFundsRepository   
from src.database import async_session_maker


router = APIRouter(prefix="/transfers", tags=["Transfers"])

#GET /{transfer_id}  # Получить перевод
#POST /  # Создать перевод
#GET / # Список переводов (с фильтрами)


#GET /{transfer_id}  # Получить перевод
#Создаем ручку где будет получать перевод
@router.get("/{transfer_id}")
#Создаем асихронную функцию куда передадим один параметр
async def get_transfer(transfer_id: int):
     # Открываем сессию с базой данных
    async with async_session_maker() as session:
        # Создаем репозиторий для работы с переводами
        repo = MoveFundsRepository(MoveFundsOrm, session)
    # Ищем перевод по ID в базе данных
    transfer = await repo.get_by_id(transfer_id)
    #Если перевод не найден, то вернем ошибку 404
    if not transfer:
        raise HTTPException(status_code=404, detail="Transfer not found")
    # Возвращаем найденный перевод
    return transfer

# Ручка для создания нового перевода
@router.post("")
async def create_transfer(transfer_data: MoveFundsCreate):
    # Открываем сессию с базой данных
    async with async_session_maker() as session:
        # Создаем репозиторий для работы с переводами
        repo = MoveFundsRepository(MoveFundsOrm, session)
        
        # Создаем новый перевод в базе данных, преобразуя схему в словарь
        transfer = await repo.create(transfer_data.model_dump())
        
        # Если создание не удалось - возвращаем ошибку 400
        if not transfer:
            raise HTTPException(status_code=400, detail="Failed to create transfer")
        
        # Возвращаем сообщение об успехе и созданные данные
        return {"message": "Transfer successfully created", "data": transfer}

# Ручка для получения списка переводов с фильтрацией
@router.get("")
async def get_list_transfers(
    donor_account: Optional[str] = None,        # Фильтр по счету отправителя
    recipient_account: Optional[str] = None,    # Фильтр по счету получателя
    date_from: Optional[date] = None,           # Фильтр от какой даты
    date_to: Optional[date] = None,             # Фильтр до какой даты
    max_amount: Optional[float] = None,         # Фильтр максимальная сумма
):
    # Открываем сессию с базой данных
    async with async_session_maker() as session:
        # Создаем репозиторий для работы с переводами
        repo = MoveFundsRepository(MoveFundsOrm, session)
        
        # Проверяем фильтры по приоритету и возвращаем результат
        
        # Если указан счет отправителя - ищем все переводы с этого счета
        if donor_account:
            transfers = await repo.get_by_field("donor_account_number", donor_account)
            return {"transfers": transfers}
            
        # Если указан счет получателя - ищем все переводы на этот счет
        if recipient_account:
            transfers = await repo.get_by_field("recipient_account_number", recipient_account)
            return {"transfers": transfers}
            
        # Если указан диапазон дат - ищем переводы в этом периоде
        if date_from and date_to:
            transfers = await repo.get_by_date_range("creation_date", date_from, date_to)
            return {"transfers": transfers}
        elif date_from:  # Только начальная дата - до сегодня
            transfers = await repo.get_by_date_range("creation_date", date_from, date.today())
            return {"transfers": transfers}
            
        # Если указана максимальная сумма - ищем переводы до этой суммы
        if max_amount:
            transfers = await repo.get_by_numeric_range("amount", 0, max_amount)
            return {"transfers": transfers}
            
        # Если фильтры не указаны - возвращаем все переводы
        transfers = await repo.get_all()
        return {"transfers": transfers}