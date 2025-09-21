from fastapi import APIRouter, HTTPException


from src.schemas.topping_cashiers import TopCashiersCreate
from src.database import async_session_maker
from src.repositories.other_repositories.topping_cashiers import TopCashiersRepository
from src.models.topping_cashiers import TopCashiersOrm

router = APIRouter(prefix="/top-cashiers", tags=["Top cashiers"])

# GET /{id} - получить пополнение по ID
@router.get("/{replenishment_id}")
async def get_replenishment(replenishment_id: int):
    # Открываем сессию с базой данных
    async with async_session_maker() as session:
        # Создаем репозиторий для работы с пополнениями
        repo = TopCashiersRepository(TopCashiersOrm, session)
        
        # Ищем пополнение по ID в базе данных
        replenishment = await repo.get_by_id(replenishment_id)
        
        # Если пополнение не найдено - возвращаем ошибку 404
        if not replenishment:
            raise HTTPException(status_code=404, detail="Replenishment not found")
        
        # Возвращаем найденное пополнение
        return replenishment

# POST / - создать новое пополнение
@router.post("")
async def create_replenishment(replenishment_data: TopCashiersCreate):
    # Открываем сессию с базой данных
    async with async_session_maker() as session:
        # Создаем репозиторий для работы с пополнениями
        repo = TopCashiersRepository(TopCashiersOrm, session)
        
        # Создаем новое пополнение в базе данных
        replenishment = await repo.create(replenishment_data.model_dump())
        
        # Если создание не удалось - возвращаем ошибку 400
        if not replenishment:
            raise HTTPException(status_code=400, detail="Failed to create replenishment")
        
        # Возвращаем сообщение об успехе и созданные данные
        return {"message": "Replenishment successfully created", "data": replenishment}

# GET / - получить список активных пополнений
@router.get("")
async def get_active_replenishments():
    # Открываем сессию с базой данных
    async with async_session_maker() as session:
        # Создаем репозиторий для работы с пополнениями
        repo = TopCashiersRepository(TopCashiersOrm, session)
        
        # Получаем все активные (неудаленные) пополнения используя специализированный метод
        replenishments = await repo.get_active_replenishments()
        
        # Возвращаем список пополнений
        return {"replenishments": replenishments}

# DELETE /{id} - отменить пополнение (soft delete)
@router.delete("/{replenishment_id}")
async def delete_replenishment(replenishment_id: int):
    # Открываем сессию с базой данных
    async with async_session_maker() as session:
        # Создаем репозиторий для работы с пополнениями
        repo = TopCashiersRepository(TopCashiersOrm, session)
        
        # Проверяем существует ли пополнение
        replenishment = await repo.get_by_id(replenishment_id)
        if not replenishment:
            raise HTTPException(status_code=404, detail="Replenishment not found")
        
        # Выполняем мягкое удаление используя специализированный метод
        deleted_replenishment = await repo.soft_delete_replenishment(replenishment_id)
        
        # Возвращаем подтверждение удаления
        return {"message": "Replenishment successfully deleted", "data": deleted_replenishment}