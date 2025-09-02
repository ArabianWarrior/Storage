from decimal import Decimal # Это Python тип для работы с числами
from src.repositories.base import BaseRepository
from src.models.manual_replenishments import ManualRepleOrm
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
#from sqlalchemy import Numeric  # Это класс для описания колонок БД
# Numeric не предназначен для аннотаций типов в функциях!


#Создадим класс который будет наследоваться от базового репозитория
class ManualRepleRepository(BaseRepository):
    #Будет работать с асихронщиной
    def __init__(self, db: AsyncSession):
        #Сохраним подключение к базе и к модели
        super().__init__(db, ManualRepleOrm)

    #Получить пополнение по номеру пополнения
    async def get_by_replenishment_number(self, replenishment_number: str) -> Optional[ManualRepleOrm]:
        result = await self.get_by_field("replenishment_number", replenishment_number)
        return result[0] if result else None

    #Получить список пополнений
    async def get_by_account_number(self, account_number: str) -> List[ManualRepleOrm]:
        return await self.get_by_field("account_number", account_number)
    
    #Метод считает денежную сумму
    async def get_total_amount_by_account(self, account_number: str) -> Optional[Decimal]:
        return await self.sum_by_field("amount", {"account_number": account_number})
