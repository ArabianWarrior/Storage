from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class RelationshipMainReturnBase(BaseModel):

    main_warehouse: str = Field(max_length=100, description="Склад основной")
    return_warehouse: str = Field(max_length=100, description="Склад возврата")

    model_config = ConfigDict(from_attributes=True)

class RelationshipMainReturnAdd(RelationshipMainReturnBase):
    pass 

class RelationshipMainReturnRead(RelationshipMainReturnBase):

    id: int

class RelationshipMainReturnUpdate(BaseModel):

    main_warehouse: Optional[str] = Field(None, max_length=100, description="Склад основной")
    return_warehouse: Optional[str] = Field(None, max_length=100, description="Склад возврата")
