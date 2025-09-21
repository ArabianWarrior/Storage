from typing import Annotated
from fastapi import Depends, HTTPException, Query, Request

from src.services.auth import AuthService
from src.utils.db_manager import DBManager
from src.database import async_session_maker


def get_pagination_params(
    page: Annotated[int, Query(1, ge=1)] = 1,
    per_page: Annotated[int, Query(10, ge=1, le=30)] = 10
) -> dict:
    return {"page": page, "per_page": per_page}

PaginationDep = Annotated[dict, Depends(get_pagination_params)]


def get_token(request: Request) -> str:
    #Делаем запрос на получение cookie файлов
    token = request.cookies.get("access_token", None)
    #Если его нет
    if not token:
        #Выкидываем ошибку
        raise HTTPException(status_code=401, detail="Вы не предоставили токен доступа")
    #401 - ошибка означает что пользователь не аутентифицирован 
    
    #И если токен есть, то просто его вернем
    return token


def get_current_user_id(token: str = Depends(get_token)) -> int:
    data = AuthService().decode_token(token)
    return data["user_id"]

UserIdDep = Annotated[int, Depends(get_current_user_id)]

def get_db_manager():
    return 

async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db

DBDep = Annotated[DBManager, Depends(get_db)]