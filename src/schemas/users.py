from pydantic import BaseModel, ConfigDict


class UserRequestAdd(BaseModel):
    email: str
    nickname: str
    password: str


class UserAdd(BaseModel):
    email: str
    nickname: str
    hashed_password: str


class User(BaseModel):
    id: int
    email: str
 
    model_config = ConfigDict(from_attributes=True)