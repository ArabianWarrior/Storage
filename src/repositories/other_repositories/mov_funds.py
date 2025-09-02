from typing import List, Optional
from src.repositories.base import BaseRepository
from src.models.mov_funds import MoveFundsOrm
from sqlalchemy.ext.asyncio import AsyncSession

#Таким образом этот код говорит
#Создай репозиторий для работы с переводом средств
#который умеет все то же что и базовый репозиторий
#плюс будет иметь все свои специальные методы



#Создаю новый класс, который наследуется от BaseRepository
class MoveFundsRepository(BaseRepository):
    #Определяю конструктор класса - метод который вызывается при создании объекта
    #db: AsyncSession - параметр для подключения к базе данных
    #def __init__ - специальный метод Python, автоматически вызывается при MoveFundsRepository(db)
    def __init__(self, db: AsyncSession):
        #super() - получить доступ к родительскому классу (BaseRepository)
        #Вызываю конструктор родительского класса и передаю ему нужные параметры
        super().__init__(db, MoveFundsOrm)
        #db - передать подключение к базе данных

    #Получить перевод по номеру перевода
    async def get_by_transfer_number(self, transfer_number: str) -> Optional[MoveFundsOrm]:
        result = await self.get_by_field("transfer_number", transfer_number)
        return result[0] if result else None
   