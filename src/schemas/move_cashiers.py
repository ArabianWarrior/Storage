from datetime import date, time
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class MoveCashiersBase(BaseModel):

    transfer_number: str = Field(max_length=50, description="Номер перевода")
    donor_cashier: str = Field(max_length=100, description="Кассир донор")
    recipient_cashier: str = Field(max_length=100, description="Кассир рецепиент")
    creation_date: date = Field(description="Дата создания")
    creation_time: time = Field(description="Время создания")
    performed_by: str = Field(max_length=100, description="Выполнил перевод")
    amount: Decimal = Field(description="Сумма")

    model_config = ConfigDict(from_attributes=True)

class MoveCashiersAdd(MoveCashiersBase):
    pass 

class MoveCashiersRead(MoveCashiersBase):

    id: int

class MoveCashiersUpdate(BaseModel):

    transfer_number: Optional[str] = Field(None, max_length=50, description="Номер перевода")
    donor_cashier: Optional[str] = Field(None, max_length=100, description="Кассир донор")
    recipient_cashier: Optional[str] = Field(None, max_length=100, description="Кассир рецепиент")
    creation_date: Optional[date] = Field(None, description="Дата создания")
    creation_time: Optional[time] = Field(None, description="Время создания")
    performed_by: Optional[str] = Field(None, max_length=100, description="Выполнил перевод")
    amount: Optional[Decimal] = Field(None, description="Сумма")
