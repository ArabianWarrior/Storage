from src.database import Base, engine_null_pool 
from src.config import settings

import pytest

#Здесь импортируются все модели данных
from src.models import *

#В начале у нас прогоняется файл conftest.py
#И только потом все остальные файлы


#Как вызвать эту функцию?
#Существует очень круто метод, называется fixture
#autouse=True - означает что нужно автоматически запустить функцию
@pytest.fixture(autouse=True)
async def async_main():
    #Пишем здесь assert, для проверки правильно ли все работает
    #Если эта функция работает не верно
    #То assert остановит операцию
    assert settings.MODE == "TEST"
    #И не даст дальше выполиться функции,
    #То есть часть которая внизу
    
    async with engine_null_pool.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        #metadata - это атрибут класса Base, мы везде от него наследуемся
        #в metadata - сохраняется информация о всех таблицах которые у нас есть