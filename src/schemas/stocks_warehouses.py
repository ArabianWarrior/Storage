from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class StocksWarehousesBase(BaseModel):
    warehouse: str = Field(max_length=100, description="Склад")
    material: str = Field(max_length=100, description="Материал")
    quantity_kg: Decimal = Field(description="Количество (кг)")
    actual_cost: Decimal = Field(description="Стоимость (факт)")
    planned_cost: Decimal = Field(description="Стоимость (план)")

    model_config = ConfigDict(from_attributes=True)


class StocksWarehousesAdd(StocksWarehousesBase):
    pass


class StocksWarehousesRead(StocksWarehousesBase):
    id: int


class StocksWarehousesUpdate(BaseModel):
    warehouse: Optional[str] = Field(None, max_length=100, description="Склад")
    material: Optional[str] = Field(None, max_length=100, description="Материал")
    quantity_kg: Optional[Decimal] = Field(None, description="Количество (кг)")
    actual_cost: Optional[Decimal] = Field(None, description="Стоимость (факт)")
    planned_cost: Optional[Decimal] = Field(None, description="Стоимость (план)")
