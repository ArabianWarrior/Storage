from datetime import date, time
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class MoveFundsBase(BaseModel):

    transfer_number: str = Field(max_length=50, description="Номер перевода")
    donor_account_number: str = Field(max_length=50, description="Расчетный счет донор")
    recipient_account_number: str = Field(max_length=50, description="Расчетный счет рецепиент")
    creation_date: date = Field(description="Дата создания")
    creation_time: time = Field(description="Время создания")
    performed_by: str = Field(max_length=100, description="Выполнил перевод")
    amount: Decimal = Field(description="Сумма")

    model_config = ConfigDict(from_attributes=True)

class MoveFundsAdd(MoveFundsBase):
    pass 


class MoveFundsRead(MoveFundsBase):

    id: int


class MoveFundsUpdate(BaseModel):

    transfer_number: Optional[str] = Field(None, max_length=50, description="Номер перевода")
    donor_account_number: Optional[str] = Field(None, max_length=50, description="Расчетный счет донор")
    recipient_account_number: Optional[str] = Field(None, max_length=50, description="Расчетный счет рецепиент")
    creation_date: Optional[date] = Field(None, description="Дата создания")
    creation_time: Optional[time] = Field(None, description="Время создания")
    performed_by: Optional[str] = Field(None, max_length=100, description="Выполнил перевод")
    amount: Optional[Decimal] = Field(None, description="Сумма")

