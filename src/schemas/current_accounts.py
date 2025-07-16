from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class CurrentAccountsBase(BaseModel):
    
    account_number: str = Field(max_length=50, description="Рассчетный счет")
    balance_on_account: Decimal = Field(description="Остаток на рассчетный счет")
    
    model_config = ConfigDict(from_attributes=True)

class CurrentAccountsAdd(CurrentAccountsBase):
    pass 

class CurrentAccountsRead(CurrentAccountsBase):

    id: int


class CurrentAccountsUpdate(BaseModel):

    account_number: Optional[str] = Field(None, description="Рассчетный счет")
    balance_on_account: Optional[Decimal] = Field(None, description="Остаток на рассчетный счет")