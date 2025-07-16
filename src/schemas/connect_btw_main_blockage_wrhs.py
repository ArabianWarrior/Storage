from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class ConnBtwMainBlockageWrhsBase(BaseModel):

    main_warehouse: str = Field(max_length=100, description="Склад основной")
    contaminated_warehouse: str = Field(max_length=100, description="Склад засор")

    model_config = ConfigDict(from_attributes=True)

class ConnBtwMainBlockageWrhsAdd(ConnBtwMainBlockageWrhsBase):
    pass 

class ConnBtwMainBlockageWrhsRead(ConnBtwMainBlockageWrhsBase):

    id: int


class ConnBtwMainBlockageWrhsUpdate(BaseModel):

    main_warehouse: Optional[str] = Field(None, description="Склад основной")
    contaminated_warehouse: Optional[str] = Field(None, description="Склад засор")

