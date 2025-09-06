from datetime import date, time
from decimal import Decimal
from typing import Optional


from pydantic import BaseModel, Field, ConfigDict


class ManualRepleBase(BaseModel):

    replenishment_number: str = Field(max_length=50, description="Номер пополнения")
    account_number: str = Field(max_length=50, description="Рассчетный счет")
    creation_date: date = Field(description="Дата создания")
    creation_time: time = Field(description="Время создания")
    created_by: str = Field(max_length=100, description="Создал")
    amount: Decimal = Field(description="Сумма")
    delete_indicator: bool = Field(description="Индикатор удаления")

    model_config = ConfigDict(from_attributes=True)

class ManualRepleCreate(BaseModel):
    replenishment_number: str = Field(max_length=50, description="Номер пополнения")
    account_number: str = Field(max_length=50, description="Расчетный счет")
    creation_date: date = Field(description="Дата создания")
    creation_time: time = Field(description="Время создания")
    created_by: str = Field(max_length=100, description="Создал")
    amount: Decimal = Field(description="Сумма")



class ManualRepleAdd(ManualRepleBase):
    pass 


class ManualRepleRead(ManualRepleBase):

    id: int


class ManualRepleUpdate(BaseModel):

    replenishment_number: Optional[str] = Field(None, max_length=50, description="Номер пополнения")
    account_number: Optional[str]= Field(None, max_length=50, description="Рассчетный счет")
    creation_date: Optional[date] = Field(None, description="Дата создания")
    creation_time: Optional[time] = Field(None, description="Время создания")
    created_by: Optional[str] = Field(None, max_length=100, description="Создал")
    amount: Optional[Decimal] = Field(None, description="Сумма")
    delete_indicator: Optional[bool] = Field(None, description="Индикатор удаления")


