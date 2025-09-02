from decimal import Decimal
from typing import Optional
from src.repositories.base import BaseRepository
from src.models.positions_shipping_certificates import PositionsShippingCertificatesOrm
from sqlalchemy.ext.asyncio import AsyncSession

class PositionsShippingCertificatesRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PositionsShippingCertificatesOrm)

    # Метод вычисляет общую стоимость отгрузки склада для всех позиций конкретного акта
    # Принимает номер акта, возвращает сумму денег или None если акт не найден
    async def get_total_warehouse_shipping_cost(self, act_number: str) -> Optional[Decimal]:
    # Вызываем базовый метод sum_by_field() с двумя параметрами:
    # 1. "warehouse_shipping_cost" - название поля которое нужно просуммировать
    #    В каждой позиции акта есть стоимость отгрузки склада, мы суммируем все эти значения
    # 2. {"act_number": act_number} - фильтр для поиска нужных записей
    #    Ищем только те позиции, где номер акта равен переданному параметру
    #    Например, если передали "ACT-2024-001", найдем только позиции этого акта
    
    # Базовый метод выполнит SQL запрос типа:
    # SELECT SUM(warehouse_shipping_cost) FROM positions_shipping_certificates WHERE act_number = 'переданный_номер'
    
    # Возвращаем результат суммирования:
    # - Если акт найден и у него есть позиции - вернется общая сумма (например, 15000.50)
    # - Если акт не найден или у него нет позиций - вернется None
        return await self.sum_by_field("warehouse_shipping_cost", {"act_number": act_number})
    
    # Метод вычисляет общий вес нетто для всех позиций конкретного акта
    # Принимает номер акта, возвращает общий вес или None если акт не найден
    async def get_total_net_weight_by_act(self, act_number: str) -> Optional[Decimal]:
        # Вызываем базовый метод sum_by_field() с двумя параметрами:
        # 1. "net_weight_kg" - название поля которое нужно просуммировать
        #    В каждой позиции акта есть вес нетто в килограммах, мы суммируем все эти веса
        # 2. {"act_number": act_number} - фильтр для поиска нужных записей
        #    Ищем только те позиции, где номер акта равен переданному параметру
        #    Например, если передали "ACT-2024-001", найдем только позиции этого акта
        
        # Базовый метод выполнит SQL запрос типа:
        # SELECT SUM(net_weight_kg) FROM positions_shipping_certificates WHERE act_number = 'переданный_номер'
        
        # Возвращаем результат суммирования:
        # - Если акт найден и у него есть позиции - вернется общий вес (например, 1250.75)
        # - Если акт не найден или у него нет позиций - вернется None
        return await self.sum_by_field("net_weight_kg", {"act_number": act_number})