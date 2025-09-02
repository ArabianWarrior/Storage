from typing import Any, List, Optional
from pydantic import BaseModel
from sqlalchemy import asc, delete, desc, func, insert, or_, select, update, values
from sqlalchemy import in_
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, db: AsyncSession, model:type):
        self.db = db
        self.model = model


    # self.model означает "модель ЭТОГО конкретного репозитория"

    async def _get_field(self, field_name: str):
        """
        Проверяет, что модель имеет атрибут с именем field_name
        и возвращает его; иначе бросает AttributeError.
        """
        if not hasattr(self.model, field_name):
            raise AttributeError(f"Модель {self.model.__name__} не имеет поля {field_name}")
        return getattr(self.model, field_name)

    async def get_by_id(self, id: int):
        stmt = select(self.model).where(self.model.id == id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_all(self):
        stmt = select(self.model)
        result = await self.db.execute(stmt)
        return result.scalars().all()
    

    #Метод получает на вход уже проверенные данные 
    # (это специальный объект Pydantic, который гарантирует что данные правильные)
    async def create(self, data: BaseModel):
        #Говорим "хочу вставить в эту таблицу"
        #Превращаем наш объект с данными в обычный словарь
        #Говорим базе "и верни мне обратно то, что создалось"
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        #Отправляем подготовленную команду в базу данных и ждем результат
        result = await self.db.execute(stmt)
        #Говорим базе данных "теперь сохрани это окончательно" (иначе изменения пропадут)
        await self.db.commit()
        #Из того что вернула база данных, 
        # достаем созданную запись и отдаем тому кто вызвал метод
        return result.scalar_one()



    # Метод "мягкого" удаления - помечает запись как удаленную, не удаляя физически
    async def soft_delete(self, id: int, deletion_field: str = "is_deleted"):
        check_field = self._get_field(deletion_field)
    # Строим команду для базы данных:
        stmt = (
        update(self.model) #"Хочу обновить записи в этой таблице"
        .where(self.model.id == id) #"Но только ту запись, у которой ID равен переданному"
        .values({deletion_field: True}) #"Установи в поле удаления значение True"
        .returning(self.model) #"И верни мне обратно обновленную запись целиком"
    )
    # Отправляем команду в базу данных и ждем результат
        result = await self.db.execute(stmt)
    # Сохраняем изменения окончательно
        await self.db.commit()
    # Возвращаем обновленную запись или None если запись не найдена
        return result.scalar_one_or_none()
    


    #Метод обновляет существующую запись в базе данных по её id
    # Получает id записи, новые данные и флаг нужно ли исключать пустые поля
    async def update_by_id(self, id: int, data: BaseModel, exclude_unset: bool = True):
    # Превращаем объект с данными в словарь
    # exclude_unset=True означает "не включай поля, которые не были заданы"
    # (например, если в data есть поле name, но оно не было установлено, то его не включим)
        update_data = data.model_dump(exclude_unset=exclude_unset)
    # Строим команду для базы данных:
        stmt = (
            update(self.model)  # "Хочу обновить записи в этой таблице"
            .where(self.model.id == id)  # "Но только ту запись, у которой id равен переданному"
            .values(**update_data) # "Установи в ней эти новые значения"
            .returning(self.model)    # "И верни мне обратно обновленную запись целиком"
        )
    # Отправляем команду в базу данных и ждем результат
        result = await self.db.execute(stmt)
    # Говорим базе "теперь сохрани изменения окончательно"
        await self.db.commit()
    # Достаем обновленную запись из результата
    # scalar_one_or_none() означает "дай мне одну запись, а если её нет - верни None"
    # (в отличие от scalar_one(), который упадет с ошибкой если записи нет)
        return result.scalar_one_or_none()



    # Метод удаляет запись из базы данных по её ID
    async def delete_by_id(self, id: int):
    # Строим команду: "удали запись с этим ID и верни что удалилось"
        stmt = (
        delete(self.model)
        .where(self.model.id == id)
        .returning(self.model)
    )
    # Выполняем команду в базе данных
        result = await self.db.execute(stmt)
    # Сохраняем изменения окончательно
        await self.db.commit()
    # Возвращаем удаленную запись или None если ничего не нашли
        return result.scalar_one_or_none()



    # Метод восстанавливает "мягко удаленную" запись
    async def restore_soft_deleted(self, id: int, deletion_field: str = "is_deleted"):
    # Проверяем есть ли поле у модели
        check_field = self._get_field(deletion_field)

    # Получаем объект поля для SQL запроса
        field = getattr(self.model, deletion_field)
    # Строим команду: восстанови запись если она была удалена
        stmt = (
        update(self.model) # "Хочу обновить записи в этой таблице"
        .values({deletion_field: False}) # "Установи в указанном поле значение False"
        .where(             # "Но только для записей которые соответствуют условиям:"
            (self.model.id == id) &   # "ID записи равен переданному параметру"
            (field == True)  # "И поле удаления сейчас равно True (запись помечена как удаленная)"
        )
        .returning(self.model)   # "И верни мне обратно обновленную запись целиком"
    )
    # Выполняем команду в базе данных
        result = await self.db.execute(stmt)
    # Сохраняем изменения
        await self.db.commit()
    # Возвращаем восстановленную запись или None
        return result.scalar_one_or_none()

    
    async def get_all_activate(self, deletion_field: str = "is_deleted"):
        check_field = self._get_field(deletion_field)

    # Получаем ссылку на поле модели (например, User.is_deleted)
    # Теперь field — это как указатель на столбец в SQL-таблице
        field = getattr(self.model, deletion_field)
    # Готовим SQL-запрос:
    # 1. select(self.model) — "выбрать все поля из таблицы"
    # 2. where(field == False) — "но только где is_deleted = False"
        stmt = select(self.model).where(field == False)
    # Отправляем запрос в базу данных
    # Важно: execute() только выполняет запрос, но не возвращает данные сразу
        result = await self.db.execute(stmt)
        return result.scalars().all()



    # Метод ищет все записи в таблице где указанное поле равно нужному значению
    async def get_by_field(self, field_name, value):
        check_field = self._get_field(field_name)
    # Получаем это поле из описания таблицы чтобы использовать в запросе
        field = getattr(self.model, field_name)
    # Строим команду для базы данных: найди все записи где это поле равно этому значению
        #select(self.model) покажи мне все строки из этой таблицы, 
        # where(field == value) = но только те где в этой колонке лежит это значение
        stmt = select(self.model).where(field == value)
    # Отправляем команду в базу данных и ждем ответ
        result = await self.db.execute(stmt)
    # Достаем все найденные записи из ответа и возвращаем их списком
        return result.scalars().all()
       

    # 1. Объяви асинхронную функцию которая принимает любое количество именованных параметров через **filters
    async def get_by_multiple(self, **filters):
    # 2. Создай пустой список для хранения всех условий поиска
        conditions = []
    # 3. Начни цикл который пройдется по каждой паре "название_поля: значение" из переданных фильтров
        for field_name, value in filters.items():
    # 4. Внутри цикла: проверь существует ли текущее поле в модели, если нет - выброси ошибку
            if not hasattr(self.model, field_name):
                raise AttributeError(f"Модель {self.model} не имеет поля {field_name}")
    # 5. Получи объект поля из модели по его названию
            field = getattr(self.model, field_name)        
    # 6. Создай условие "поле == значение" и добавь его в список условий
            conditions.append(field == value)
    # 7. После цикла: построй SELECT запрос который ищет записи где выполняются ВСЕ условия (используй *conditions чтобы распаковать список)
        stmt = select(self.model).where(*conditions)
    # 8. Выполни запрос в базе данных   
        result = await self.db.execute(stmt)
    # 9. Верни все найденные записи списком
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
    


    # Метод ищет записи в базе данных по тексту в нескольких полях одновременно
    # Например: найти всех пользователей, у которых "Иван" есть в имени ИЛИ в email
    async def search_by_text(self, search_query: str, search_fields: list):
        # Проверяем не пустой ли текст для поиска
        # Если пустой - нет смысла искать, возвращаем пустой список
        if not search_query:
            return []
        
        # Проверяем передали ли нам поля для поиска
        # Если список полей пустой - искать негде, возвращаем пустой список
        if not search_fields:
            return []
    
        # Проверяем что все поля из списка действительно существуют в нашей таблице
        # Проходимся по каждому названию поля
        for search_field in search_fields:
            # Спрашиваем у модели: "А есть ли у тебя поле с таким названием?"
            if not hasattr(self.model, search_field):
                # Если поля нет - ругаемся и останавливаем выполнение
                raise AttributeError(f"Модель {self.model} не имеет поля {search_field}")
    
        # Создаем пустой список для хранения всех условий поиска
        # В него мы будем складывать условия типа "name содержит 'Иван'" или "email содержит 'Иван'"
        conditions = []
        
        # Проходимся по каждому полю и создаем для него условие поиска
        for search_field in search_fields:
            # Получаем объект поля из описания таблицы (чтобы с ним можно было работать в SQL)
            field = getattr(self.model, search_field)
            
            # Создаем условие поиска: "в этом поле должен содержаться наш текст"
            # ilike - это поиск без учета регистра (большие/маленькие буквы не важны)
            # % с двух сторон означает "любые символы до и после нашего текста"
            # Например: %Иван% найдет "Иван", "Иванов", "Петр Иванович"
            like = field.ilike(f"%{search_query}%")
            
            # Добавляем это условие в наш общий список условий
            conditions.append(like)
        
        # Строим команду для базы данных:
        # select(self.model) = "покажи мне все записи из этой таблицы"
        # where(or_(*conditions)) = "но только те, где выполняется ЛЮБОЕ из условий"
        # or_(*conditions) означает "условие1 ИЛИ условие2 ИЛИ условие3..."
        stmt = select(self.model).where(or_(*conditions))
        
        result = await self.db.execute(stmt)
        return result.scalars().all()
    

    # Метод находит все записи где дата в указанном поле лежит между двумя заданными датами
    # Например: найти всех пользователей зарегистрированных в январе, или заказы за неделю
    async def get_by_date_range(self, date_field, start_date, end_date):
        # Проверяем логику дат: начальная дата не может быть позже конечной
        # Если кто-то передал "от завтра до вчера" - это бессмыслица
        if start_date > end_date:
            return []  # Возвращаем пустой список, чтобы не ломать программу
    
        # Проверяем существует ли указанное поле в нашей модели
        # Если поля нет - нельзя по нему фильтровать, ругаемся ошибкой
        if not hasattr(self.model, date_field):
            raise AttributeError(f"Модель {self.model} не имеет {date_field}")
    
        # Получаем объект поля из модели по его названию
        # Теперь field - это не просто строка, а SQL-объект с которым можно работать
        field = getattr(self.model, date_field)
        
        # Строим SQL-запрос с двумя условиями:
        # select(self.model) = "покажи мне все записи из этой таблицы"
        # where() содержит два условия объединенных через И (&):
        #   field >= start_date = "дата в поле не раньше начальной даты"
        #   field <= end_date = "И не позже конечной даты"
        # Скобки важны для правильного порядка выполнения операций
        stmt = (select(self.model)
        .where((field >= start_date) &
            (field <= end_date)
        )
                )
    
        result = await self.db.execute(stmt)
        return result.scalars().all()


    # Метод ищет все записи где число в указанном поле лежит между двумя заданными значениями
    # Например: найти товары с ценой от 100 до 500 рублей, или пользователей возрастом от 18 до 65 лет
    async def get_by_numeric_range(self, field_name, min_value, max_value):
        # Проверяем логику диапазона: минимальное значение не может быть больше максимального
        # Если кто-то передал "от 500 до 100" - это бессмыслица, возвращаем пустой список
        if min_value > max_value:
            return []
    
        # Проверяем существует ли указанное поле в нашей модели
        # Если поля нет - нельзя по нему фильтровать, ругаемся ошибкой
        if not hasattr(self.model, field_name):
            raise AttributeError(f"Модель {self.model} не имеет поля {field_name}")
    
        # Получаем объект поля из модели по его названию
        # Теперь field - это не просто строка, а SQL-объект с которым можно работать
        field = getattr(self.model, field_name)
        
        # Строим SQL-запрос с двумя условиями:
        # select(self.model) = "покажи мне все записи из этой таблицы"
        # where() содержит два условия объединенных через И (&):
        #   field >= min_value = "значение в поле не меньше минимального"
        #   field <= max_value = "И не больше максимального"
        # Скобки важны для правильного порядка выполнения операций
        stmt = (
            select(self.model)
            .where((field <= max_value) &
                (field >= min_value)
            )
        )
        
        result = await self.db.execute(stmt)
        return result.scalars().all()
    
    

    
    # Метод ищет записи где дата и время в указанном поле попадают в заданный период
    # Например: найти заказы созданные с 10:00 до 18:00, или логи за последние 2 часа
    async def get_by_datetime_range(self, datetime_field, start_datetime, end_datetime):
        # Проверяем логику периода: начальное время не может быть позже конечного
        # Если передали "с завтра до вчера" - возвращаем пустой список
        if start_datetime > end_datetime:
            return []
    
        # Проверяем есть ли такое поле в нашей таблице
        # Если поля нет - нельзя по нему искать, выбрасываем ошибку
        if not hasattr(self.model, datetime_field):
            raise AttributeError(f"Модель {self.model} не имеет поля {datetime_field}")
    
        # Получаем объект поля из модели чтобы использовать его в SQL запросе
        field = getattr(self.model, datetime_field)
        
        # Строим запрос: найди записи где дата-время лежит между двумя значениями
        # >= start_datetime означает "не раньше начального времени"
        # <= end_datetime означает "не позже конечного времени"
        # & объединяет условия через И (должны выполняться оба)
        stmt = (
            select(self.model)
            .where((field >= start_datetime) &
                    (field <= end_datetime)
                )
        )
        # Отправляем запрос в базу данных и ждем результат
        result = await self.db.execute(stmt)
        
        # Возвращаем все найденные записи списком
        return result.scalars().all()
    

    # Метод возвращает записи по страницам с информацией о пагинации
    async def get_paginated(self, page, page_size, filters=None, order_by=None):
        # Базовые проверки параметров
        if page < 1 or page_size <= 0:
            return {"items": [], "total": 0, "page": page, "page_size": page_size, "total_pages": 0}
        
        # Вычисляем offset для пагинации
        offset = (page - 1) * page_size
        
        # Строим базовый запрос
        stmt = select(self.model)
        
        # Применяем фильтры если есть
        if filters:
            conditions = []
            for field_name, value in filters.items():
                if not hasattr(self.model, field_name):
                    raise AttributeError(f"Модель {self.model} не имеет поля {field_name}")
                field = getattr(self.model, field_name)
                conditions.append(field == value)
            stmt = stmt.where(*conditions)
        
        # Подсчитываем общее количество записей
        count_stmt = select(func.count()).select_from(self.model)
        if filters:
            count_stmt = count_stmt.where(*conditions)
        
        count_result = await self.db.execute(count_stmt)
        total = count_result.scalar()
        total_pages = -(-total // page_size) if total > 0 else 0
        
        # Применяем сортировку если указана
        if order_by:
            if not hasattr(self.model, order_by):
                raise AttributeError(f"Модель {self.model} не имеет поля {order_by}")
            order_field = getattr(self.model, order_by)
            stmt = stmt.order_by(order_field)
        
        # Применяем пагинацию и выполняем запрос
        stmt = stmt.offset(offset).limit(page_size)
        result = await self.db.execute(stmt)
        items = result.scalars().all()
        
        return {
            "items": items,
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages
        }


    #Создаю функцию которая умеет сортировать
    async def get_all_sorted(self, field_name, descending = False): #"descending = False = "В каком порядке?"
        #А есть ли вообще такая колонка в таблице?
        if not hasattr(self.model, field_name):
            raise AttributeError(f"Модель {self.model} не имеет поля {field_name}")
        
        #Найди мне эту колонку в таблице
        field = getattr(self.model, field_name)
        #Определяю в каком направлении сортировать
        direction = desc(field) if descending else asc(field)
        #Составляю инструкцию для базы данных
        stmt = select(self.model).order_by(direction)

        result = await self.db.execute(stmt)
        return result.scalars().all()
    


    # Метод подсчитывает количество записей, которые соответствуют переданным фильтрам
    async def count_by_filters(self, **filters):
        # Создаем пустой список для хранения всех условий поиска
        conditions = []

        # Проходимся по каждой паре "название_поля: значение" из переданных фильтров
        for field_name, value in filters.items():
            # Проверяем существует ли текущее поле в нашей модели
            if not hasattr(self.model, field_name):
                raise AttributeError(f"Модель {self.model} не имеет поля {field_name}")
        
            # Получаем объект поля из модели по его названию
            field = getattr(self.model, field_name)
            
            # Создаем условие "поле == значение" и добавляем его в список условий
            conditions.append(field == value)

        # Строим запрос для подсчета количества записей в этой таблице
        stmt = select(func.count()).select_from(self.model)
        
        # Если есть условия фильтрации - добавляем их к запросу
        if conditions:
            stmt = stmt.where(*conditions)
        
        result = await self.db.execute(stmt)
        return result.scalar()
    
    
    async def sum_by_field(self, field_name, filters=None):
        """
        Метод вычисляет сумму всех значений в указанном поле
        Можно добавить фильтры для подсчета суммы только по определенным записям
        Например: сумма всех заказов пользователя с id=5
        """
        # Получаем объект поля с проверкой его существования
        field_obj = await self._get_field(field_name)
        
        # Строим запрос для вычисления суммы значений в этом поле
        stmt = select(func.sum(field_obj))
        
        # Если переданы фильтры - применяем их
        if filters:
            # Явно проверяем тип фильтров
            if not isinstance(filters, dict):
                raise TypeError("filters должен быть словарем")
            
            conditions = []
            for filter_field, value in filters.items():
                # Проверяем каждое поле фильтра
                filter_field_obj = await self._get_field(filter_field)
                conditions.append(filter_field_obj == value)
            
            # Добавляем условия к запросу
            if conditions:
                stmt = stmt.where(*conditions)

        result = await self.db.execute(stmt)
        
        # Возвращаем сумму или 0 если результат None (нет записей)
        sum_result = result.scalar()
        return sum_result if sum_result is not None else 0

    async def group_by_field(self, field_name, filters=None):
        """
        Метод группирует записи по указанному полю и возвращает количество в каждой группе
        Например: сколько пользователей в каждом городе, сколько заказов у каждого статуса
        """
        # Получаем объект поля с проверкой его существования
        field_obj = await self._get_field(field_name)
        
        # Строим запрос: выбираем поле для группировки и считаем количество в каждой группе
        stmt = select(field_obj, func.count().label('count')).group_by(field_obj)
        
        # Если переданы фильтры - применяем их ПЕРЕД группировкой
        if filters:
            # Явно проверяем тип фильтров
            if not isinstance(filters, dict):
                raise TypeError("filters должен быть словарем")
            
            conditions = []
            for filter_field, value in filters.items():
                filter_field_obj = await self._get_field(filter_field)
                conditions.append(filter_field_obj == value)
            
            # Добавляем условия к запросу
            if conditions:
                stmt = stmt.where(*conditions)
        
        # Выполняем запрос
        result = await self.db.execute(stmt)
        
        # Возвращаем результат как список кортежей: [(значение, количество), ...]
        return result.all()

    async def create_many(self, data_list):
        """
        Метод создает много записей за один раз (bulk insert)
        Более эффективно чем создавать записи по одной в цикле
        """
        # Проверяем что передали не пустой список
        if not data_list:
            return []
        
        # Преобразуем список объектов в список словарей
        values_list = []
        for data in data_list:
            if hasattr(data, 'model_dump'):  # Это Pydantic модель
                values_list.append(data.model_dump())
            elif isinstance(data, dict):  # Это уже словарь
                values_list.append(data)
            else:
                raise TypeError("Элементы data_list должны быть Pydantic моделями или словарями")
        
        # Строим команду массовой вставки
        stmt = insert(self.model).values(values_list).returning(self.model)
        result = await self.db.execute(stmt)
        await self.db.commit()
        return result.scalars().all()

    async def update_many(self, filters, update_data):
        """
        Метод обновляет много записей одновременно по заданным фильтрам
        Например: повысить зарплату всем сотрудникам отдела "IT"
        """
        # Проверяем что переданы и фильтры и данные для обновления
        if not filters or not update_data:
            return []
        
        # Проверяем тип фильтров
        if not isinstance(filters, dict):
            raise TypeError("filters должен быть словарем")
        
        # Готовим условия фильтрации
        conditions = []
        for field_name, value in filters.items():
            field_obj = await self._get_field(field_name)
            conditions.append(field_obj == value)
        
        # Готовим данные для обновления
        if hasattr(update_data, 'model_dump'):  # Pydantic модель
            update_dict = update_data.model_dump(exclude_unset=True)
        elif isinstance(update_data, dict):  # Обычный словарь
            update_dict = update_data
        else:
            raise TypeError("update_data должен быть Pydantic моделью или словарем")
        
        # Проверяем что все поля для обновления существуют в модели
        for field_name in update_dict.keys():
            await self._get_field(field_name)  # Проверка существования поля
        
        # Строим команду массового обновления
        stmt = (
            update(self.model)
            .where(*conditions)  # Применяем все условия фильтрации
            .values(**update_dict)  # Устанавливаем новые значения
            .returning(self.model)  # Возвращаем обновленные записи
        )
        
        result = await self.db.execute(stmt)
        await self.db.commit()
        return result.scalars().all()

    async def exists_by_field(self, field_name: str, value: str):
        """
        Метод проверяет существует ли запись с указанным значением в указанном поле
        Возвращает True если запись найдена, False если нет
        """
        # Получаем объект поля с проверкой его существования
        field_obj = await self._get_field(field_name)
        
        # Строим запрос для проверки существования
        stmt = select(func.count()).select_from(self.model).where(field_obj == value)
        result = await self.db.execute(stmt)
        count = result.scalar()
        
        # Возвращаем True если найдена хотя бы одна запись
        return count > 0

    async def exists_by_multiple_fields(self, **filters):
        """
        Метод проверяет существует ли запись которая соответствует всем переданным условиям
        Например: есть ли пользователь с email='test@test.com' И статусом='active'
        """
        # Проверяем что переданы условия для проверки
        if not filters:
            return False
        
        # Проверяем тип фильтров
        if not isinstance(filters, dict):
            raise TypeError("filters должен быть словарем")
        
        # Готовим условия для поиска
        conditions = []
        for field_name, value in filters.items():
            field_obj = await self._get_field(field_name)
            conditions.append(field_obj == value)
        
        # Строим запрос для подсчета записей соответствующих всем условиям
        stmt = select(func.count()).select_from(self.model).where(*conditions)
        result = await self.db.execute(stmt)
        
        # Получаем количество найденных записей
        count = result.scalar()
        
        # Возвращаем True если найдена хотя бы одна запись
        return count > 0
    
    #Метод говорит - “дай значение нужной колонки для конкретной позиции конкретного акта”.
    #Асинхронная функция принимающая 3 параметра
    """Аналогия
    Представь шкаф с папками (акты). В каждой папке — листы (позиции). Ты говоришь архивариусу:
    “Папка ACT-2024-0153, лист №2, скажи цену за кг по факту.”
    Он находит папку, нужный лист и зачитывает конкретное поле."""
    async def act_and_position_number(self, act_number: str, position_number: int, field_name: str) -> Optional[Any]:
        #Создаем запрос к таблице
        stmt = (select(self.model)
                #выбираем записи с заданными act_number и position_number 
                .where(
                    self.model.act_number == act_number,
                    self.model.position_number == position_number
                )
                )
        #Выполняем запрос в базе данных
        result = await self.db.execute(stmt)
        #Получаем первую запись из результата
        record = result.scalars().first()

        #Если запись не найдена, возвращаем None
        if record is None:
            return None
        #Иначе возвращаем значение нужного поля
        return getattr(record, field_name)