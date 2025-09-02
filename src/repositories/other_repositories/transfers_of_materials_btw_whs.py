from typing import Optional
from src.repositories.base import BaseRepository
from src.models.transfers_of_materials_btw_whs import TransfersMaterialsBtwWhsOrm
from sqlalchemy.ext.asyncio import AsyncSession

class TransfersMaterialsBtwWhsRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TransfersMaterialsBtwWhsOrm)


    #Получить перевод по номеру перевода
    async def get_by_transfer_number(self, transfer_number: str) -> Optional[TransfersMaterialsBtwWhsOrm]:
        result = await self.get_by_field("transfer_number", transfer_number)
        return result[0] if result else None