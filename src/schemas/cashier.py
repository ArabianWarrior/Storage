from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class CahiersBase(BaseModel):

    cashier_name: str = Field(max_length=100, description="Кассир")
    cash_balance: Decimal = Field(description="Остаток на кассире")

    model_config = ConfigDict(from_attributes=True)

class CashiersAdd(CahiersBase):
    pass 

class CashiersRead(CahiersBase):

    id: int

class CashiersUpdate(BaseModel):

    cashier_name: Optional[str] = Field(None, description="Кассир")
    cash_balance: Optional[Decimal] = Field(None, description="Остаток на кассире")

