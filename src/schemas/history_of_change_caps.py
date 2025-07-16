from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class HistoryChangeCapBase(BaseModel):
    material: str = Field(max_length=100, description="Наименование материала")
    current_price_cash: Decimal = Field(description="Актуальная цена (наличный расчет)")
    current_price_cashless: Decimal = Field(description="Актуальная цена (безналичный расчет)")
    entered_by: str = Field(max_length=100, description="Кто ввел данные")
    entry_date: datetime = Field(description="Дата ввода")

    model_config = ConfigDict(from_attributes=True)

class HistoryChangeCapAdd(HistoryChangeCapBase):
    pass

class HistoryChangeCapRead(HistoryChangeCapBase):
    
    id: int

class HistoryChangeCapUpdate(BaseModel):
    
    material: Optional[str] = Field(None, description="Наименование материала")
    current_price_cash: Optional[Decimal] = Field(None, description="Актуальная цена (наличный расчет)")
    current_price_cashless: Optional[Decimal] = Field(None, description="Актуальная цена (безналичный расчет)")
    entered_by: Optional[str] = Field(None, description="Кто ввел данные")
    entry_date: Optional[datetime] = Field(None, description="Дата ввода")

