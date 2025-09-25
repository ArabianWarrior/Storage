from src.repositories.other_repositories.application_payments import ApplicationsPaymentRepository
from src.repositories.other_repositories.users import UsersRepository
from src.repositories.other_repositories.manual_replenishments import ManualRepleRepository
from src.repositories.other_repositories.mov_funds import MoveFundsRepository
from src.repositories.other_repositories.positions_shipping_certificates import PositionsShippingCertificatesRepository
from src.repositories.other_repositories.shipping_certificates import ShippingCertificatesRepository
from src.repositories.other_repositories.topping_cashiers import TopCashiersRepository
from src.repositories.other_repositories.transfers_of_materials_btw_whs import TransfersMaterialsBtwWhsRepository

class DBManager:

    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.application = ApplicationsPaymentRepository(self.session)
        self.users = UsersRepository(self.session)
        self.manual = ManualRepleRepository(self.session)
        self.move = MoveFundsRepository(self.session)
        self.position = PositionsShippingCertificatesRepository(self.session)
        self.shipping = ShippingCertificatesRepository(self.session)
        self.topping = TopCashiersRepository(self.session)
        self.transfers = TransfersMaterialsBtwWhsRepository(self.session)

        return self
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Если была ошибка - откатываем
            await self.session.rollback()
        else:
            # Если всё хорошо - коммитим (для тестов)
            await self.session.commit()
        await self.session.close()