from sqlalchemy import insert

from asyncpg import UniqueViolationError

from app.validation.model_user import User
from app.config.settings import session_maker, my_logger
from app.database.models import *


async def add_user(user: User) -> None:
    """
    Асинхронная функция для работы с базой данных.
    Добавляет пользователя в базу данных.

    :param user: Объект класса User.
    """

    try:
        async with session_maker() as session:
            query = insert(SearchCompanion).values(user.model_dump())

            await session.execute(query)

            await session.commit()

            return my_logger.info(f'Пользователь {user.telegram_id} добавлен в поиск собеседников!')

    except UniqueViolationError:
        my_logger.error(f'Ошибка уникальности, при добавлении пользователя {user.telegram_id}')
