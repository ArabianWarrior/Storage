from datetime import date, datetime, time
from decimal import Decimal
from typing import Optional

from pydantic import Field, BaseModel, ConfigDict


class ShippingCertificatesBase(BaseModel):
    act_number: str = Field(max_length=50, description="Номер акта")
    creation_date: date = Field(description="Дата создания")
    creation_time: time = Field(description="Время создания")
    shipment_date: datetime = Field(description="Дата отгрузки")
    counterparty: str = Field(max_length=100, description="Контрагент")
    warehouse: str = Field(max_length=100, description="Склад")
    created_by: str = Field(max_length=100, description="Создал")
    status: str = Field(max_length=50, description="Статус")
    rejection_reason: str = Field(max_length=200, description="Причина отклонения (индикатор)")
    vehicle_number: str = Field(max_length=50, description="Номер автомобиля")
    deletion_indicator: bool = Field(description="Индикатор удаления")
    planned_sum: Decimal = Field(description="Сумма по акту (план)")
    actual_sum: Decimal = Field(description="Сумма по акту (факт)")
    actual_balance: Decimal = Field(description="Остаток (факт)")
    paid_status: bool = Field(description="Погасили (факт)")

    model_config = ConfigDict(from_attributes=True)

class ShippingCertificatesCreate(BaseModel):
    act_number: str = Field(max_length=50)
    creation_date: date
    creation_time: time  
    shipment_date: datetime
    counterparty: str = Field(max_length=100)
    warehouse: str = Field(max_length=100)
    planned_sum: Decimal

    # Необязательные поля
    status: str = Field(default="В работе", max_length=50)
    created_by: Optional[str] = Field(None, max_length=100)
    vehicle_number: Optional[str] = Field(None, max_length=50)


class ShippingCertificatesAdd(ShippingCertificatesBase):
    pass


class ShippingCertificatesRead(ShippingCertificatesBase):
    id: int


class ShippingCertificatesUpdate(BaseModel):
    
    act_number: Optional[str] = Field(None, max_length=50, description="Номер акта")
    creation_date: Optional[date] = Field(None, description="Дата создания")
    creation_time: Optional[time] = Field(None, description="Время создания")
    shipment_date: Optional[datetime] = Field(None, description="Дата отгрузки")
    counterparty: Optional[str] = Field(None, max_length=100, description="Контрагент")
    warehouse: Optional[str] = Field(None, max_length=100, description="Склад")
    created_by: Optional[str] = Field(None, max_length=100, description="Создал")
    status: Optional[str] = Field(None, max_length=50, description="Статус")
    rejection_reason: Optional[str] = Field(None, max_length=200, description="Причина отклонения (индикатор)")
    vehicle_number: Optional[str] = Field(None, max_length=50, description="Номер автомобиля")
    deletion_indicator: Optional[bool] = Field(None, description="Индикатор удаления")
    planned_sum: Optional[Decimal] = Field(None, description="Сумма по акту (план)")
    actual_sum: Optional[Decimal] = Field(None, description="Сумма по акту (факт)")
    actual_balance: Optional[Decimal] = Field(None, description="Остаток (факт)")
    paid_status: Optional[bool] = Field(None, description="Погасили (факт)")
