from typing import Optional
from src.repositories.base import BaseRepository
from src.models.users import UsersOrm
from sqlalchemy.ext.asyncio import AsyncSession

class UsersRepositiory(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, UsersOrm)

    async def get_by_email(self, email: str) -> Optional[UsersOrm]:
        result = await self.get_by_field("email", email)
        return result[0] if result else None
    
    
    # async def get_user_with_hashed_password(self, email: EmailStr):
    #     query = select(self.model).filter_by(email=email)
    #     result = await self.session.execute(query)
    #     model =  result.scalars().one()
    #     return UserWithHashedPass.model_validate(model)
            