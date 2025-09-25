from src.schemas.application_payments import ApplicationPaymentsCreate
from src.utils.db_manager import DBManager
from src.database import async_session_maker


async def test_create_application():
    create_application = ApplicationPaymentsCreate(
        application_number="Двадцать",
        act_number="номер 3",
        issued_amount=500000,
        payment_method="Карта",
        payment_source="Прибыль организации",
        created_by="Марк Абрамов")
    #Используем наш DBManager, для более комфортной эксплуатации
    async with DBManager(session_factory=async_session_maker) as db:
        new_application_data = await db.application.add(create_application)
        await db.commit()
        print(f"{new_application_data=}")    

