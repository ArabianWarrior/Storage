from typing import Optional
from src.repositories.base import BaseRepository
from src.models.application_payments import ApplicationsPaymentOrm
from sqlalchemy.ext.asyncio import AsyncSession


class ApplicationsPaymentRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ApplicationsPaymentOrm)
    
    async def get_by_application_number(self, application_number: str) -> Optional[ApplicationsPaymentOrm]:
        """Получить приложение по номеру приложения"""
        return await self.get_by_field("application_number", application_number)
   
    async def get_by_act_number(self, act_number: str) -> list[ApplicationsPaymentOrm]:
        """Получить приложения по номеру акта"""
        return await self.get_by_field("act_number", act_number)
   
    async def get_by_created_by(self, created_by: str) -> list[ApplicationsPaymentOrm]:
        """Получить приложения по создателю"""
        result = await self.get_by_field("created_by", created_by)
   
    async def get_by_payment_method(self, payment_method: str) -> list[ApplicationsPaymentOrm]:
        """Получить приложения по способу оплаты"""
        return await self.get_by_field("payment_method", payment_method)
   
    async def get_by_payment_source(self, payment_source: str) -> list[ApplicationsPaymentOrm]:
        """Получить приложения по источнику оплаты"""
        return await self.get_by_field("payment_source", payment_source)