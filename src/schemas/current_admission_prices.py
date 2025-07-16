from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict



class CurrentAdmissionPricesBase(BaseModel):

    material: str = Field(max_length=100, description="Наименование материала")
    current_price_cash: Decimal = Field(description="Актуальная цена (наличный расчет)")
    current_price_cashless: Decimal = Field(description="Актуальная цена (безналичный расчет)")

    model_config = ConfigDict(from_attributes=True)

class CurrentAdmissionPricesAdd(CurrentAdmissionPricesBase):
    pass 


class CurrentAdmissionPricesRead(CurrentAdmissionPricesBase):

    id: int


class CurrentAdmissionPricesUpdate(BaseModel):

    material: Optional[str] = Field(None, description="Наименование материала")
    current_price_cash: Optional[Decimal] = Field(None, description="Актуальная цена (наличный расчет)")
    current_price_cashless: Optional[Decimal] = Field(None, description="Актуальная цена (безналичный расчет)")

