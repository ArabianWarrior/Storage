
from decimal import Decimal
from typing import List, Optional
from src.repositories.base import BaseRepository
from src.models.cashiers import CashiersOrm
from sqlalchemy.ext.asyncio import AsyncSession


class CashiersRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        #Инициализация репозитория: говорим базовому классу, с какой моделью работать
        super().__init__(db, CashiersOrm)


    async def get_by_cashier_name(self, cashier_name: str) -> Optional[CashiersOrm]:
        """Метод ищет кассира по его имени.
        Если найдено несколько кассиров с одинаковым именем, то возвращает первого
        Если никто не найден - возвращает None"""
        #Ищем всех кассиров с таким именем (обычно должен быть один)
        result = await self.get_by_field("cashier_name", cashier_name)
        #Если кто-то нашелся - берем первого, если никто нет - возвращаем None
        return result[0] if result else None
    
    async def get_by_cash_balance(self, min_balance: float, max_balance: float) -> List[Decimal]:
        """Метод ищет кассиров по диапазону остатка на кассе.
        Возвращает список кассиров, у которых cash_balance между min_balance и max_balance."""
        #Используем метод из базового репозитория, для поиска по диапазону числового поля
        return await self.get_by_numeric_range("cash_balance", min_balance, max_balance,)



    #List[Decimal] — если тебе нужен только остаток на кассе, 
    # без всей информации о кассире. Тогда внутри метода нужно выбрать именно поле cash_balance.