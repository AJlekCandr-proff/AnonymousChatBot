from sqlalchemy import select

from app.database.models.users import Profiles
from app.config.settings import async_session, my_logger


async def selects_users() -> list[Profiles]:
    """
    Асинхронная функция для извлечения пользователей, которые находятся в поиске собеседника.

    :return: Список объектов класса User.
    """

    try:
        async with async_session() as session:
            query = select(Profiles).where(Profiles.in_search is True)

            result = await session.execute(query)
            list_users_in_search = result.scalars().all()

            return list_users_in_search

    except Exception as error:
        my_logger.error(f'Ошибка при извлечении пользователей в базе данных {error}')


async def selects_user(user_id: int) -> Profiles:
    """
    Асинхронная функция для проверки наличия пользователя в поиске собеседника.

    :return: Объект класса User.
    """

    try:
        async with async_session() as session:
            query = select(Profiles).where(Profiles.telegram_id == user_id)

            result = await session.execute(query)
            user = result.scalar()

            return user

    except Exception as error:
        my_logger.error(f'Ошибка при извлечении пользователей в базе данных {error}')
