from sqlalchemy import select

from app.database.models.users import SearchCompanion
from app.validation.model_user import User
from app.config.settings import async_session, my_logger


async def selects_users() -> list[User]:
    """
    Асинхронная функция для извлечения пользователей, которые находятся в поиске собеседника.

    :return: Список объектов класса User.
    """

    try:
        async with async_session() as session:
            query = select(SearchCompanion)

            result = await session.execute(query)
            list_users_in_search = result.scalars().all()

            return list_users_in_search

    except Exception as error:
        my_logger.error(f'Ошибка при извлечении пользователей в базе данных {error}')


