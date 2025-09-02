from decimal import Decimal
from typing import Optional

from sqlalchemy import select
from src.repositories.base import BaseRepository
#"Привези мне модель (описание таблицы) для позиций актов"
from src.models.act_positions import ActPositionsOrm
#"Привези мне тип для подключения к базе данных"
from sqlalchemy.ext.asyncio import AsyncSession

#"Мой репозиторий умеет всё то же что и базовый, плюс что-то своё"
class ActPositionsRepository(BaseRepository):
    #"Когда кто-то создает мой репозиторий" - вызывается эта функция
    def __init__(self, db: AsyncSession): #db = подключение к базе данных (передается извне)
#super() = "обращаюсь к родительскому классу" (BaseRepository)
        super().__init__(db, ActPositionsOrm)

    
    async def fact_price_per_kg(self, act_position: str, position_number: int) -> Optional[Decimal]:
        return await self.act_and_position_number(act_position, position_number, "fact_price_per_kg")

    async def plan_price_per_kg(self, act_position: str, position_number: int) -> Optional[Decimal]:
        return await self.act_and_position_number(act_position, position_number, "plan_price_per_kg")
    
    async def contamination_percent(self, act_position: str, position_number: int) -> Optional[Decimal]:
        return await self.act_and_position_number(act_position, position_number, "contamination_percent")
    
    async def contamination_kg(self, act_position: str, position_number: int) -> Optional[Decimal]:
        return await self.act_and_position_number(act_position, position_number, "contamination_kg")
    
    async def net_weight_kg(self, act_position: str, position_number: int) -> Optional[Decimal]:
        return await self.act_and_position_number(act_position, position_number, "net_weight_kg")
    
    async def planned_cost(self, act_position: str, position_number: int) -> Optional[Decimal]:
        return await self.act_and_position_number(act_position, position_number, "planned_cost")
    
    async def actual_cost(self, act_position: str, position_number: int) -> Optional[Decimal]:
        return await self.act_and_position_number(act_position, position_number, "actual_cost")
    
    async def material(self, act_position: str, position_number: int) -> Optional[str]:
        return await self.act_and_position_number(act_position, position_number, "material")
    
    async def gross_weight_kg(self, act_position: str, position_number: int) -> Optional[float]:
        return await self.act_and_position_number(act_position, position_number, "gross_weight_kg")