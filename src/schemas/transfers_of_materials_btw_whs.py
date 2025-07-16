from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class TransfersMaterialsBtwWhsBase(BaseModel):
    transfer_number: str = Field(max_length=50, description="Номер перевода")
    transfer_date: datetime = Field(description="Дата перевода")
    transfer_time: datetime = Field(description="Время перевода")
    executed_by: str = Field(max_length=100, description="Кто выполнил перевод")
    from_warehouse: str = Field(max_length=100, description="Из склада")
    to_warehouse: str = Field(max_length=100, description="В склад")
    from_material: str = Field(max_length=100, description="Из материала")
    to_material: str = Field(max_length=100, description="В материал")
    quantity_kg: float = Field(description="Количество (кг)")
    material_cost: float = Field(description="Стоимость переводимого материала")
    planned_material_cost: float = Field(description="Стоимость итогового материала по плану")

    model_config = ConfigDict(from_attributes=True)


class TransfersMaterialsBtwWhsAdd(TransfersMaterialsBtwWhsBase):
    pass


class TransfersMaterialsBtwWhsRead(TransfersMaterialsBtwWhsBase):
    id: int


class TransfersMaterialsBtwWhsUpdate(BaseModel):
    transfer_number: Optional[str] = Field(None, max_length=50, description="Номер перевода")
    transfer_date: Optional[datetime] = Field(None, description="Дата перевода")
    transfer_time: Optional[datetime] = Field(None, description="Время перевода")
    executed_by: Optional[str] = Field(None, max_length=100, description="Кто выполнил перевод")
    from_warehouse: Optional[str] = Field(None, max_length=100, description="Из склада")
    to_warehouse: Optional[str] = Field(None, max_length=100, description="В склад")
    from_material: Optional[str] = Field(None, max_length=100, description="Из материала")
    to_material: Optional[str] = Field(None, max_length=100, description="В материал")
    quantity_kg: Optional[float] = Field(None, description="Количество (кг)")
    material_cost: Optional[float] = Field(None, description="Стоимость переводимого материала")
    planned_material_cost: Optional[float] = Field(None, description="Стоимость итогового материала по плану")
