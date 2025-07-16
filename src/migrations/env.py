import asyncio
import sys

# Решение для Windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from logging.config import fileConfig

from sqlalchemy import pool


from alembic import context

from src.models import *  
from src.models.acceptance_certificates import AcceptanceCertificatesOrm
from src.models.act_positions import ActPositionsOrm
from src.models.text_reasons_rejects import ReasonsRejectOrm
from src.models.application_payments import ApplicationsPaymentOrm
from src.models.current_admission_prices import CurrentAdmissionPricesOrm
from src.models.history_of_change_caps import HistoryChangeCapOrm
from src.models.transfers_of_materials_btw_whs import TransfersMaterialsBtwWhsOrm
from src.models.shipping_certificates import ShippingCertificatesOrm
from src.models.positions_shipping_certificates import PositionsShippingCertificatesOrm
from src.models.text_reasons_rejecting_shipping_certificates import TextsReasonsRejectingShipCrfOrm
from src.models.app_pay_ship_crfs import AppPayShipCrfsOrm
from src.models.stocks_warehouses import StocksWarehousesOrm
from src.models.connect_btw_main_blockage_wrhs import ConnBtwMainBlockageWrhsOrm
from src.models.rlt_btw_m_wrh_rts import RelationshipMainReturnOrm
from src.models.costs import CostrsOrm
from src.models.current_accounts import CurrentAccountsOrm
from src.models.mov_funds import MoveFundsOrm
from src.models.manual_replenishments import ManualRepleOrm
from src.models.cashiers import CashiersOrm
from src.models.move_cashiers import MoveCashiersOrm
from src.models.topping_cashiers import TopCashiersOrm
from src.models.users import UsersOrm


from src.database import Base
from src.config import settings



config = context.config

config.set_main_option("sqlalchemy.url", f"{settings.DB_URL}?async_fallback=True")


if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Перезагрузите метаданные
Base.metadata.reflect = None
Base.metadata.clear()

target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    from sqlalchemy.ext.asyncio import create_async_engine
    from sqlalchemy.ext.asyncio import AsyncConnection

    # Создаем асинхронный движок
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    async def run_async_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)

    # Запускаем асинхронные миграции
    asyncio.run(run_async_migrations())

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True
    )
    
    with context.begin_transaction():
        context.run_migrations()