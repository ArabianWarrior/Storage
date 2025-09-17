from sqlalchemy import select

from pydantic import EmailStr
from src.repositories.base import BaseRepository
from src.models.users import UsersOrm
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.users import  User, UserWithHashedPass

class UsersRepositiory(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, UsersOrm)
    model = UsersOrm
    schema = User

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = select(self.model).filter_by(email=email)
        result = await self.session.execute(query)
        model = result.scalars().one()
        return UserWithHashedPass.model_validate(model)



    
