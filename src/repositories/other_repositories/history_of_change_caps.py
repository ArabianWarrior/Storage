from typing import List, Optional
from src.repositories.base import BaseRepository
from src.models.history_of_change_caps import HistoryChangeCapOrm
from sqlalchemy.ext.asyncio import AsyncSession


class HistoryChangeCapRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        #Сохраняем подключение к базе и модели
        super().__init__(db, HistoryChangeCapOrm)

    #Асинхронная функция которая ищет цены по точному названию материала
    #Принимает: название материала (строка)
    #Возвращает: найденную запись с ценами или None если материал не найден
    async def get_by_material(self, material: str) -> Optional[HistoryChangeCapOrm]:
        #Используем готовый метод из базового репозитория
        #Ищем в поле "material" значение равное переданному параметру
        return await self.get_by_field("material", material)
    
    #Асинхронная функция которая ищет материалы по частичному совпадению названия
    #Принимает: часть названия материала для поиска (строка)
    #Возвращает: список всех найденных записей с ценами(может быть пустой список)
    async def search_materials(self, search_query: str) -> List[HistoryChangeCapOrm]:
        #Используем уже готовый метод из базового репозитория
        #Ищем в поле material все записи содержащие search_query 
        return await self.search_by_text(search_query, ["material"])
        