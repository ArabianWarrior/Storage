from typing import Optional
from src.repositories.base import BaseRepository
from src.models.connect_btw_main_blockage_wrhs import ConnBtwMainBlockageWrhsOrm
from sqlalchemy.ext.asyncio import AsyncSession



class ConnBtwMainBlockageWrhsRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ConnBtwMainBlockageWrhsOrm)

    async def get_by_main_warehouse(self, main_warehouse: str) -> Optional[ConnBtwMainBlockageWrhsOrm]:
        result = await self.get_by_field("main_warehouse", main_warehouse)
        #result[0] if result else None возвращает первую запись, если что-то найдено, иначе None.
        return result[0] if result else None
    

    async def get_by_contaminated_warehouse(self, contaminated_warehouse: str) -> Optional[ConnBtwMainBlockageWrhsOrm]:
        result = await self.get_by_field("contaminated_warehouse", contaminated_warehouse)
        return result[0] if result else None
    
    #Важно помнить:
    #Используем result[0] if result else None везде, где ожидаем один объект, а базовый метод возвращает список объектов.