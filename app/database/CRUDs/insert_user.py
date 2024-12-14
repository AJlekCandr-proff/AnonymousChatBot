from sqlalchemy import insert

from asyncpg.exceptions import UniqueViolationError
from sqlalchemy.exc import IntegrityError

from app.validation.model_user import User
from app.config.settings import async_session, my_logger
from app.database.models import *


async def add_user(user: User) -> None:
    """
    Асинхронная функция для работы с базой данных.
    Добавляет пользователя в базу данных.

    :param user: Объект класса User.
    """

    try:
        async with async_session() as session:
            query = insert(SearchCompanion).values(user.model_dump())

            await session.execute(query)

            await session.commit()

            return my_logger.info(f'Пользователь {user.telegram_id} добавлен в поиск собеседников!')

    except Exception as error:
        my_logger.error(f'При добавлении пользователя в таблицу поиска собеседника произошла ошибка: {error}')
