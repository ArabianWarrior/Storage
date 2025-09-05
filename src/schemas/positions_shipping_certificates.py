from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class PositionsShippingCertificatesBase(BaseModel):
    act_number: str = Field(max_length=50, description="Номер акта")
    position_number: int = Field(description="Номер позиции")
    material: str = Field(max_length=100, description="Материал")
    gross_weight_kg: Decimal = Field(description="Вес брутто (кг)")
    psa_shipping_price_per_kg: Decimal = Field(description="Цена отгрузки ПСА (за кг)")
    warehouse_shipping_price_per_kg: Decimal = Field(description="Цена отгрузки склад (за кг)")
    contamination_percent: Decimal = Field(description="Засор (%)")
    contamination_kg: Decimal = Field(description="Засор (кг)")
    return_kg: Decimal = Field(description="Возврат (кг)")
    net_weight_kg: Decimal = Field(description="Вес нетто (кг)")
    warehouse_shipping_cost: Decimal = Field(description="Стоимость отгрузки склада")
    psa_shipping_cost: Decimal = Field(description="Стоимость отгрузки ПСА")

    model_config = ConfigDict(from_attributes=True)

class PositionsShippingCertificatesCreate(BaseModel):
    # Обязательные поля
    act_number: str = Field(max_length=50, description="Номер акта")
    position_number: int = Field(description="Номер позиции")
    material: str = Field(max_length=100, description="Материал")
    gross_weight_kg: Decimal = Field(description="Вес брутто (кг)")

    #Опциональные поля
    psa_shipping_price_per_kg: Optional[Decimal] = Field(None, description="Цена отгрузки ПСА (за кг)")
    warehouse_shipping_price_per_kg: Optional[Decimal] = Field(None, description="Цена отгрузки склад (за кг)")
    contamination_percent: Optional[Decimal] = Field(None, description="Засор (%)")
    contamination_kg: Optional[Decimal] = Field(None, description="Засор (кг)")
    return_kg: Optional[Decimal] = Field(None, description="Возврат (кг)")
    net_weight_kg: Optional[Decimal] = Field(None, description="Вес нетто (кг)")
    warehouse_shipping_cost: Optional[Decimal] = Field(None, description="Стоимость отгрузки склада")
    psa_shipping_cost: Optional[Decimal] = Field(None, description="Стоимость отгрузки ПСА")
    

class PositionsShippingCertificatesAdd(PositionsShippingCertificatesBase):
    pass


class PositionsShippingCertificatesRead(PositionsShippingCertificatesBase):
    id: int


class PositionsShippingCertificatesUpdate(BaseModel):
    act_number: Optional[str] = Field(None, max_length=50, description="Номер акта")
    position_number: Optional[int] = Field(None, description="Номер позиции")
    material: Optional[str] = Field(None, max_length=100, description="Материал")
    gross_weight_kg: Optional[Decimal] = Field(None, description="Вес брутто (кг)")
    psa_shipping_price_per_kg: Optional[Decimal] = Field(None, description="Цена отгрузки ПСА (за кг)")
    warehouse_shipping_price_per_kg: Optional[Decimal] = Field(None, description="Цена отгрузки склад (за кг)")
    contamination_percent: Optional[Decimal] = Field(None, description="Засор (%)")
    contamination_kg: Optional[Decimal] = Field(None, description="Засор (кг)")
    return_kg: Optional[Decimal] = Field(None, description="Возврат (кг)")
    net_weight_kg: Optional[Decimal] = Field(None, description="Вес нетто (кг)")
    warehouse_shipping_cost: Optional[Decimal] = Field(None, description="Стоимость отгрузки склада")
    psa_shipping_cost: Optional[Decimal] = Field(None, description="Стоимость отгрузки ПСА")
