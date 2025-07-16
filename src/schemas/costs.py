from datetime import date, time
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CostsBase(BaseModel):
    
    expense: Decimal = Field(description="Расход")
    payment_method: str = Field(max_length=20, description="Способ оплаты")
    payment_source: str = Field(max_length=100, description="Источник оплаты")
    amount_rub: Decimal = Field(description="Сумма руб")
    comment: str = Field(max_length=255, description="Комментарий")
    created_date: date = Field(description="Дата создания")
    created_time: time = Field(description="Время создания")
    created_by: str = Field(max_length=100, description="Создал")
    deletion_indicator: bool = Field(description="Индикатор удаления")
    deleted_date: Optional [date] = Field(None, description="Дата удаления")
    deleted_time: Optional [time] = Field(None, description="Время удаления")
    deleted_by: Optional [str] = Field(None, max_length=100, description="Удалил")
    
    model_config = ConfigDict(from_attributes=True)

class CostsAdd(CostsBase):
    pass 

class CostsRead(CostsBase):

    id: int

class CostsUpdate(BaseModel):

    expense: Optional[Decimal] = Field(None, description="Расход")
    payment_method: Optional[str] = Field(None, description="Способ оплаты")
    payment_source: Optional[str] = Field(None, description="Источник оплаты")
    amount_rub: Optional[Decimal] = Field(None, description="Сумма руб")
    comment: Optional[str] = Field(None, description="Комментарий")
    created_date: Optional[date] = Field(None, description="Дата создания")
    created_time: Optional[time] = Field(None, description="Время создания")
    created_by: Optional[str] = Field(None, max_length=100, description="Создал")
    deletion_indicator: Optional[bool] = Field(None, description="Индикатор удаления")
    deleted_date: Optional[date] = Field(None, description="Дата удаления")
    deleted_time: Optional[time] = Field(None, description="Время удаления")
    deleted_by: Optional[str] = Field(None, max_length=100, description="Удалил")


