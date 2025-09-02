from typing import Optional
from src.repositories.base import BaseRepository
from src.models.shipping_certificates import ShippingCertificatesOrm
from sqlalchemy.ext.asyncio import AsyncSession


class ShippingCertificatesRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ShippingCertificatesOrm)

    async def get_by_act_number(self, act_number: str) -> Optional[ShippingCertificatesOrm]:
        result = await self.get_by_field("act_number", act_number)
        return result[0] if result else None