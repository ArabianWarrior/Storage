from datetime import date, time
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class TopCashiersBase(BaseModel):
    replenishment_number: str = Field(max_length=50, description="Номер пополнения")
    cashier: str = Field(max_length=100, description="Кассир")
    creation_date: date = Field(description="Дата")
    creation_time: time = Field(description="Время")
    created_by: str = Field(max_length=100, description="Создал")
    amount: Decimal = Field(description="Сумма")
    delete_indicator: bool = Field(False, description="Индикатор удаления")

    model_config = ConfigDict(from_attributes=True)


class TopCashiersAdd(TopCashiersBase):
    pass


class TopCashiersRead(TopCashiersBase):
    id: int


class TopCashiersUpdate(BaseModel):
    replenishment_number: Optional[str] = Field(None, max_length=50, description="Номер пополнения")
    cashier: Optional[str] = Field(None, max_length=100, description="Кассир")
    creation_date: Optional[date] = Field(None, description="Дата создания")
    creation_time: Optional[time] = Field(None, description="Время создания")
    created_by: Optional[str] = Field(None, max_length=100, description="Создал")
    amount: Optional[Decimal] = Field(None, description="Сумма")
    delete_indicator: Optional[bool] = Field(None, description="Индикатор удаления")
