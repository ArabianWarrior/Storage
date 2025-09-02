from decimal import Decimal
from typing import List, Optional
from src.repositories.base import BaseRepository
from src.models.costs import CostrsOrm
from sqlalchemy.ext.asyncio import AsyncSession


class CostsRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        # Сохраняем подключение к базе и модель расходов
        super().__init__(db, CostrsOrm)

    # 1. Поиск всех записей по способу оплаты
    # Берем способ оплаты
    # Ищем все записи с таким способом оплаты
    # Возвращаем список всех найденных записей
    async def get_by_payment_method(self, payment_method: str) -> List[CostrsOrm]:
        return await self.get_by_field("payment_method", payment_method)

    # 2. Поиск всех записей по источнику оплаты
    # Берем источник оплаты
    # Ищем все записи с таким источником
    # Возвращаем список всех найденных записей
    async def get_by_payment_source(self, payment_source: str) -> List[CostrsOrm]:
        return await self.get_by_field("payment_source", payment_source)

    # 3. Поиск одной записи по создателю
    # Берем имя пользователя
    # Ищем все записи с таким создателем
    # Если нашли хотя бы одну запись — берем первую
    # Если не нашли — возвращаем None
    async def get_created_by(self, created_by: str) -> Optional[CostrsOrm]:
        result = await self.get_by_field("created_by", created_by)
        return result[0] if result else None

    # 4. Поиск расходов по диапазону суммы
    # Берем минимальную и максимальную сумму
    # Ищем все записи, у которых amount_rub между min и max
    # Возвращаем список всех найденных записей
    async def get_amount_rub(self, min_amount: float, max_amount: float) -> List[CostrsOrm]:
        return await self.get_by_numeric_range("amount_rub", min_amount, max_amount)

    # 5. Поиск расходов по диапазону расхода
    # Берем минимальный и максимальный расход
    # Ищем все записи, у которых expense между min и max
    # Возвращаем список всех найденных записей
    async def get_by_expense(self, min_expense: float, max_expense: float) -> List[CostrsOrm]:
        return await self.get_by_numeric_range("expense", min_expense, max_expense)

    # 6. Поиск расходов за период по дате
    # Берем поле даты, дату начала и дату конца
    # Ищем все записи, у которых дата в этом диапазоне
    # Возвращаем список всех найденных записей
    async def get_by_date_range(self, date_field, start_date, end_date) -> List[CostrsOrm]:
        return await super().get_by_date_range(date_field, start_date, end_date)

    # 🔹 Правила для будущих репозиториев:
    # - List[Модель] → когда возвращается несколько записей
    # - Optional[Модель] → когда возвращается одна запись или None
    # - result[0] if result else None → используем для Optional, чтобы взять первую запись или вернуть None
    # - Диапазоны чисел и дат → всегда List, потому что может быть много совпадений
