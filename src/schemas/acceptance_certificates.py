from datetime import date, datetime, time
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class AcceptanceCertificatesBase(BaseModel):
    act_number: str = Field(max_length=50,description="Номер акта")
    date_creation: date = Field(description="Дата создания акта")
    creation_time: time = Field(description="Время создания акта")
    date_admission: datetime = Field(description="Дата поступления")
    counterparty_name: str = Field(description="Наименование контрагента")
    storage: str = Field(description="Склад")
    status: str = Field(description="Статус акта")
    reason_rejection: Optional[str] = None 
    deletion_indicator: bool = False
    amount_according_act_plan: Decimal = Field(description="Сумма по акту (план)")
    amount_according_act_fact: Decimal = Field(description="Сумма по акту (факт)")
    extinguished_fact: bool = Field(description="Факт погашения")
    remainder_fact: Decimal = Field(description="Остаток (факт)")
    payment_method: str = Field(description="Способ оплаты")

    model_config = ConfigDict(from_attributes=True)


class AcceptanceCertificatesAdd(AcceptanceCertificatesBase):
    """Поля, необходимые при создании акта"""
    


class AcceptanceCertificatesRead(AcceptanceCertificatesBase):
    """Схема ответа API"""
    id: int
    created: datetime


class AcceptanceCertificatesUpdate(BaseModel):
    """Поля, которые можно менять при обновлении акта"""
     
    act_number: Optional[str] = Field(None, max_length=50,description="Номер акта")
    date_creation: Optional[date] = Field(None, description="Дата создания акта")
    creation_time: Optional[time] = Field(None,description="Время создания акта")
    date_admission: Optional[datetime] = Field(None, description="Дата поступления")
    counterparty_name: Optional[str ]= Field(None, description="Наименование контрагента")
    storage: Optional[str ]= Field(None, description="Склад")
    status: Optional[str ]= Field(None, description="Статус акта")
    reason_rejection: Optional[str] = None 
    deletion_indicator: Optional[bool] = False
    amount_according_act_plan: Optional[Decimal] = Field(None, description="Сумма по акту (план)")
    amount_according_act_fact: Optional[Decimal] = Field(None,description="Сумма по акту (факт)")
    extinguished_fact: Optional[bool] = Field(None, description="Факт погашения")
    remainder_fact: Optional[Decimal] = Field(None, description="Остаток (факт)")
    payment_method: Optional[str ]= Field(None, description="Способ оплаты")

