# src/repositories/acceptance_certificates_repository.py
from datetime import date
from decimal import Decimal
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_

from src.repositories.base import BaseRepository
from src.models.acceptance_certificates import AcceptanceCertificatesOrm


class AcceptanceCertificatesRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AcceptanceCertificatesOrm)

    async def get_by_act_number(self, act_number: str) -> Optional[AcceptanceCertificatesOrm]:
        """Получить акт по номеру"""
        result = await self.get_by_field("act_number", act_number)
        return result[0] if result else None

    async def get_by_status(self, status: str) -> List[AcceptanceCertificatesOrm]:
        """Получить все акты по статусу"""
        return await self.get_by_field("status", status)

    async def get_by_counterparty(self, counterparty_name: str) -> List[AcceptanceCertificatesOrm]:
        """Получить все акты контрагента"""
        return await self.get_by_field("counterparty_name", counterparty_name)

    async def get_by_storage(self, storage: str) -> List[AcceptanceCertificatesOrm]:
        """Получить все акты по складу"""
        return await self.get_by_field("storage", storage)

    async def get_by_date_range(self, start_date: date, end_date: date) -> List[AcceptanceCertificatesOrm]:
        """Получить акты за период"""
        return await super().get_by_date_range("date_creation", start_date, end_date)

    async def get_by_amount_range(self, min_amount: Decimal, max_amount: Decimal) -> List[AcceptanceCertificatesOrm]:
        """Получить акты по диапазону суммы (план)"""
        return await self.get_by_numeric_range("amount_according_act_plan", min_amount, max_amount)

    async def get_pending_acts(self) -> List[AcceptanceCertificatesOrm]:
        """Получить акты со статусом 'pending' или аналогичным"""
        # Предполагаем, что есть статусы типа 'pending', 'in_progress', 'waiting'
        stmt = select(self.model).where(
            and_(
                self.model.deletion_indicator == False,
                or_(
                    self.model.status == 'pending',
                    self.model.status == 'in_progress',
                    self.model.status == 'waiting'
                )
            )
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_completed_acts(self) -> List[AcceptanceCertificatesOrm]:
        """Получить завершенные акты"""
        return await self.get_by_multiple(
            status='completed',
            deletion_indicator=False
        )

    async def get_acts_with_remainder(self) -> List[AcceptanceCertificatesOrm]:
        """Получить акты с остатком"""
        stmt = select(self.model).where(
            and_(
                self.model.deletion_indicator == False,
                self.model.remainder_fact > 0
            )
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_extinguished_acts(self) -> List[AcceptanceCertificatesOrm]:
        """Получить погашенные акты"""
        return await self.get_by_multiple(
            extinguished_fact=True,
            deletion_indicator=False
        )

    async def search_acts(self, search_query: str) -> List[AcceptanceCertificatesOrm]:
        """Поиск актов по номеру, контрагенту или складу"""
        return await self.search_by_text(
            search_query, 
            ["act_number", "counterparty_name", "storage"]
        )

    async def get_acts_by_payment_method(self, payment_method: str) -> List[AcceptanceCertificatesOrm]:
        """Получить акты по способу оплаты"""
        return await self.get_by_field("payment_method", payment_method)

    async def get_total_amount_by_status(self, status: str) -> Optional[Decimal]:
        """Получить общую сумму актов по статусу"""
        acts = await self.get_by_multiple(status=status, deletion_indicator=False)
        return sum(act.amount_according_act_fact for act in acts)

    async def soft_delete_act(self, act_id: int) -> Optional[AcceptanceCertificatesOrm]:
        """Мягкое удаление акта"""
        return await self.soft_delete(act_id, "deletion_indicator")

    async def restore_act(self, act_id: int) -> Optional[AcceptanceCertificatesOrm]:
        """Восстановление удаленного акта"""
        return await self.restore_soft_deleted(act_id, "deletion_indicator")

    async def get_active_acts(self) -> List[AcceptanceCertificatesOrm]:
        """Получить все активные (не удаленные) акты"""
        return await self.get_all_activate("deletion_indicator")