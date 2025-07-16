from datetime import date, time
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ApplicationPaymentsBase(BaseModel):
    application_number: str = Field(max_length=50, description="Номер приложения")
    act_number: str = Field(max_length=50, description="Номер акта")
    created_date: date = Field(description="Дата создания")
    created_time: time = Field(description="Время создания")
    created_by: str = Field(max_length=100, description="Создал")
    issued_amount: Decimal = Field(description="Выданная сумма (руб)")
    payment_method: str = Field(max_length=50, description="Способ оплаты")
    payment_source: str = Field(max_length=100, description="Источник оплаты")
    remaining_balance: Decimal = Field(description="Остаток на момент выдачи суммы")
    is_deleted: bool = Field(False, description="Индикатор удаления")
    deleted_date: Optional[date] = Field(None, description="Дата удаления")
    deleted_time: Optional[time] = Field(None, description="Время удаления")
    deleted_by: Optional[str] = Field(None, max_length=100, description="Удалил")

    model_config = ConfigDict(from_attributes=True)


class ApplicationPaymentsAdd(ApplicationPaymentsBase):
    pass


class ApplicationPaymentsRead(ApplicationPaymentsBase):
    id: int


class ApplicationPaymentsUpdate(BaseModel):
    application_number: Optional[str] = Field(None, max_length=50, description="Номер приложения")
    act_number: Optional[str] = Field(None, max_length=50, description="Номер акта")
    created_date: Optional[date] = Field(None, description="Дата создания")
    created_time: Optional[time] = Field(None, description="Время создания")
    created_by: Optional[str] = Field(None, max_length=100, description="Создал")
    issued_amount: Optional[Decimal] = Field(None, description="Выданная сумма (руб)")
    payment_method: Optional[str] = Field(None, max_length=50, description="Способ оплаты")
    payment_source: Optional[str] = Field(None, max_length=100, description="Источник оплаты")
    remaining_balance: Optional[Decimal] = Field(None, description="Остаток на момент выдачи суммы")
    is_deleted: Optional[bool] = Field(None, description="Индикатор удаления")
    deleted_date: Optional[date] = Field(None, description="Дата удаления")
    deleted_time: Optional[time] = Field(None, description="Время удаления")
    deleted_by: Optional[str] = Field(None, max_length=100, description="Удалил")
