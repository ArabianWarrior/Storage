from typing import List
from pydantic import BaseModel
from sqlalchemy import delete, insert, select, update, values
from sqlalchemy import in_
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db: Session, model:type):
        self.db = db
        self.model = model

    async def get_by_id(self, id: int):
        stmt = select(self.model).where(self.model.id == id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all(self):
        stmt = select(self.model)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def create(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.db.execute(stmt)
        await self.db.commit()
        return result.scalar_one()

    async def soft_delete(self, id: int, deletion_field: str = "is_deleted"):
        if not hasattr(self.model, deletion_field):
            raise AttributeError(f"Модель не поддерживает {deletion_field}")
        field = getattr(self.model, deletion_field)
        stmt = update(self.model).where(self.model.id == id).values({deletion_field: True})
        await self.db.execute(stmt)
        await self.db.commit()

    async def update_by_id(self, id: int, data: BaseModel, exclude_unset: bool = True):
        update_data = data.model_dump(exclude_unset=exclude_unset)
        stmt = (
            update(self.model)
            .where(self.model.id == id)
            .values(**update_data)
            .returning(self.model)
        )
        result = await self.db.execute(stmt)
        await self.db.commit()
        return result.scalar_one_or_none()

    async def delete_by_id(self, id: int):
        stmt = (
            delete(self.model)
            .where(self.model.id == id)
            .returning(self.model)
        )
        result = await self.db.execute(stmt)
        await self.db.commit()
        return result.scalar_one_or_none()

    async def restore_soft_deleted(self, id: int, deletion_field: str = "is_deleted"):
        if not hasattr(self.model, deletion_field):
            raise AttributeError(f"Модель {self.model.__name__} не поддерживает {deletion_field}")
        field = getattr(self.model, deletion_field)
        stmt = (
            update(self.model)
            .values({deletion_field: False})
            .where(
                (self.model.id == id) &
                (field == True)
            )
            .returning(self.model)
        )
        result = await self.db.execute(stmt)
        await self.db.commit()
        return result.scalar_one_or_none()


    async def get_all_active(self, deletion_field: str = "is_deleted"):
        if not hasattr(self.model, deletion_field):
            raise AttributeError(f"Модель {self.model} не поддерживает {deletion_field}")
        
        field = getattr(self.model, deletion_field)
        stmt = select(self.model).where(field == False)
        result = await self.db.execute(stmt)
        return result.scalars().all()
    
    async def get_by_field(self, field_name, value):
        if not hasattr(self.model, field_name):
            raise AttributeError(f"Модель {self.model} не имеет поля {field_name}")
        
        field = getattr(self.model, field_name)
        stmt = select(self.model).where(field == value)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_by_multiple_fields(self, **filters):
        conditions = []
        for field_name, value in filters.items():
            if not hasattr(self.model, field_name):
                raise AttributeError(f"Модель {self.model} не имеет поля {field_name}")
    
            field = getattr(self.model, field_name)
            conditions.append(field == value)

        stmt = select(self.model).where(*conditions)
        result = await self.db.execute(stmt)
        return result.scalars().all()
    
    async def get_by_fields_in(self, field_name: str, values_list: list):
        if not hasattr(self.model, field_name):
            raise AttributeError(f"Модель {self.model} не имеет поля {field_name}")
        
        if not isinstance(values_list, (tuple, list)):
            raise TypeError("values list должен быть списком или кортежем")
        
        if not values_list:
            return []
        
        field = getattr(self.model, field_name)
        stmt = select(self.model).where(field.in_(values_list))

        result = await self.db.execute(stmt)
        return result.scalars().all()
    
    # async def search_by_text(self, search_query, search_fields):
        