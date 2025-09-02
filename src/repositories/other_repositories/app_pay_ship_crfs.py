from decimal import Decimal
from typing import Optional
from datetime import date, time
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base import BaseRepository
from src.models.app_pay_ship_crfs import AppPayShipCrfsOrm


class AppPayShipCrfsRepository(BaseRepository):
    """
    Репозиторий для работы с приложениями по оплате актов отгрузки
    """
    
    def __init__(self, db: AsyncSession):
        super().__init__(db, AppPayShipCrfsOrm)
    
    async def get_by_application_number(self, application_number: str) -> Optional[AppPayShipCrfsOrm]:
        """Получить приложение по номеру приложения"""
        return await self.get_by_field('application_number', application_number)
    
    async def get_by_act_number(self, act_number: str) -> list[AppPayShipCrfsOrm]:
        """Получить приложения по номеру акта"""
        return await self.get_by_field('act_number', act_number)
    
    async def get_by_created_by(self, created_by: str) -> list[AppPayShipCrfsOrm]:
        """Получить приложения по создателю"""
        return await self.get_by_field('created_by', created_by)
    
    async def get_by_payment_method(self, payment_method: str) -> list[AppPayShipCrfsOrm]:
        """Получить приложения по способу оплаты"""
        return await self.get_by_field('payment_method', payment_method)