from datetime import date, time
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class TextsReasonsRejectingShipCrfBase(BaseModel):
    act_number: str = Field(max_length=50, description="Номер акта")
    rejection_reason_text: str = Field(max_length=255, description="Текст причин отклонения")
    created_by: str = Field(max_length=100, description="Создал")
    creation_date: date = Field(description="Дата создания")
    creation_time: time = Field(description="Время создания")

    model_config = ConfigDict(from_attributes=True)


class TextsReasonsRejectingShipCrfAdd(TextsReasonsRejectingShipCrfBase):
    pass


class TextsReasonsRejectingShipCrfRead(TextsReasonsRejectingShipCrfBase):
    id: int


class TextsReasonsRejectingShipCrfUpdate(BaseModel):
    act_number: Optional[str] = Field(None, max_length=50, description="Номер акта")
    rejection_reason_text: Optional[str] = Field(None, max_length=255, description="Текст причин отклонения")
    created_by: Optional[str] = Field(None, max_length=100, description="Создал")
    creation_date: Optional[date] = Field(None, description="Дата создания")
    creation_time: Optional[time] = Field(None, description="Время создания")
