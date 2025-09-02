from decimal import Decimal
from typing import Optional
from src.repositories.base import BaseRepository
from src.models.topping_cashiers import TopCashiersOrm
from sqlalchemy.ext.asyncio import AsyncSession

class TopCashiersRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TopCashiersOrm)
        
    #Получить пополнение по номеру пополнения
    async def get_by_replenishment_number(self, replenishment_number: str) -> Optional[TopCashiersOrm]:
        result = await self.get_by_field("replenishment_number", replenishment_number)
        return result[0] if result else None
    
    #Метод считает денежную сумму
    async def get_total_amount_by_cashier(self, cashier: str) -> Optional[Decimal]:
        return await self.sum_by_field("amount", {"cashier": cashier})