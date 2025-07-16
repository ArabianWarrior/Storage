from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ActPositionsBase(BaseModel):
    act_number: str = Field(max_length=50, description="Номер акта")
    position_number: int = Field(description="Номер позиции")
    material: str = Field(max_length=100, description="Материал")
    gross_weight_kg: float = Field(description="Вес брутто (кг)")
    fact_price_per_kg: Decimal = Field(description="Цена за факт (за кг)")
    plan_price_per_kg: Decimal = Field(description="Цена за план (за кг)")
    contamination_percent: float = Field(description="Засор (%)")
    contamination_kg: float = Field(description="Засор (кг)")
    net_weight_kg: float = Field(description="Вес нетто (кг)")
    planned_cost: Decimal = Field(description="Стоимость (план)")
    actual_cost: Decimal = Field(description="Стоимость (факт)")

    model_config = ConfigDict(from_attributes=True)


class ActPositionsAdd(ActPositionsBase):
    pass


class ActPositionsRead(ActPositionsBase):
    id: int


class ActPositionsUpdate(BaseModel):  # <--- тут было `ActPositionsdUpdate`, исправлено
    act_number: Optional[str] = Field(None, max_length=50, description="Номер акта")
    position_number: Optional[int] = Field(None, description="Номер позиции")
    material: Optional[str] = Field(None, max_length=100, description="Материал")
    gross_weight_kg: Optional[float] = Field(None, description="Вес брутто (кг)")
    fact_price_per_kg: Optional[Decimal] = Field(None, description="Цена за факт (за кг)")
    plan_price_per_kg: Optional[Decimal] = Field(None, description="Цена за план (за кг)")
    contamination_percent: Optional[float] = Field(None, description="Засор (%)")
    contamination_kg: Optional[float] = Field(None, description="Засор (кг)")
    net_weight_kg: Optional[float] = Field(None, description="Вес нетто (кг)")
    planned_cost: Optional[Decimal] = Field(None, description="Стоимость (план)")
    actual_cost: Optional[Decimal] = Field(None, description="Стоимость (факт)")
