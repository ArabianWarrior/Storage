from typing import Annotated
from fastapi import Depends, HTTPException, Query, Request
from pydantic import BaseModel

from src.services.auth import AuthService




class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(1, ge=1)]
    per_page: Annotated[int | None, Query(None, ge=1, lt=30)]

PaginationDep = Annotated[PaginationParams, Depends()]


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
    data = AuthService().decode_token(get_token)
    return data["user_id"]

UserIdDep = Annotated[int, Depends(get_current_user_id)]
