from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ReasonsRejectBase(BaseModel):
    act_id: int = Field(description="ID связанного акта приема")
    reason_text: str = Field(max_length=500, description="Текст причины отклонения")
    creator: str = Field(max_length=100, description="Идентификатор создателя записи")
    created_at: datetime = Field(description="Дата и время создания записи")

    model_config = ConfigDict(from_attributes=True)


class ReasonsRejectAdd(ReasonsRejectBase):
    pass


class ReasonsRejectRead(ReasonsRejectBase):
    id: int


class ReasonsRejectUpdate(BaseModel):
    act_id: Optional[int] = Field(None, description="ID связанного акта приема")
    reason_text: Optional[str] = Field(None, max_length=500, description="Текст причины отклонения")
    creator: Optional[str] = Field(None, max_length=100, description="Идентификатор создателя записи")
    created_at: Optional[datetime] = Field(None, description="Дата и время создания записи")
