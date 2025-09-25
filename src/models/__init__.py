#Здесь хранятся все модели в одном файле
#И потом мы импортируем с помощью 
#from src.models import * в файле env.py
#тоже самое мы делаем в conftest.py


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
