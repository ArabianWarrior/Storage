from typing import Optional
from decimal import Decimal
from datetime import date, time


from pydantic import BaseModel, ConfigDict, Field


class AppPayShipCrfsBase(BaseModel):
    application_number: str = Field(max_length=50, description="Номер приложения")
    act_number: str = Field(max_length=50, description="Номер акта")
    creation_date: date = Field(description="Дата создания")
    creation_time: time = Field(description="Время создания")
    created_by: str = Field(max_length=50, description="Создал")
    issued_amount_rub: Decimal = Field(description="Выданная сумма (руб)")
    payment_method: str = Field(description="Способ оплаты")
    replenishment_account: str = Field(description="Счет пополнения")
    balance_at_receiving: Decimal = Field(description="Остаток на момент получения суммы")
    deletion_indicator: bool = Field(description="Индикатор удаления")
    deletion_date: Optional[date] = Field(description="Дата удаления")
    deletion_time: Optional[time] = Field(description="Время удаления")
    deleted_by: Optional[str] = Field(description="Удалил")

    model_config = ConfigDict(from_attributes=True)

class AppPayShipCrfsAdd(AppPayShipCrfsBase):
    pass


class AppPayShipCrfsRead(AppPayShipCrfsBase):
    
    id: int



class AppPayShipCrfsUpdate(BaseModel):
    
    application_number: Optional[str] = Field(None, description="Номер приложения")
    act_number: Optional[str] = Field(None, description="Номер акта")
    creation_date: Optional[date] = Field(None, description="Дата создания")
    creation_time: Optional[time] = Field(None, description="Время создания")
    created_by: Optional[str] = Field(None, description="Создал")
    issued_amount_rub: Optional[Decimal] = Field(None, description="Выданная сумма (руб)")
    payment_method: Optional[str] = Field(None, description="Способ оплаты")
    replenishment_account: Optional[str] = Field(None, description="Счет пополнения")
    balance_at_receiving: Optional[Decimal] = Field(None, description="Остаток на момент получения суммы")
    deletion_indicator: Optional[bool] = Field(None, description="Индикатор удаления")
    deletion_date: Optional[date] = Field(None, description="Дата удаления")
    deletion_time: Optional[time] = Field(None, description="Время удаления")
    deleted_by: Optional[str] = Field(None, description="Удалил")

