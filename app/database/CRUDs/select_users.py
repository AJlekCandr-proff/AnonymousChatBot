from sqlalchemy import select

from app.database.models.users import Profiles
from app.config.settings import async_session, my_logger
from app.validation.model_user import User


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


async def select_user(user_id: int) -> User:
    """
    Асинхронная функция для проверки наличия пользователя в поиске собеседника.

    :return: Объект класса User.
    """

    try:
        async with async_session() as session:
            query = select(Profiles).where(Profiles.telegram_id == user_id)

            result = await session.execute(query)
            user: Profiles = result.scalar()

            return User(
                telegram_id=user.telegram_id,
                full_name=user.full_name,
                in_search=user.in_search,
                date=user.date,
                interests=user.interests
            )

    except Exception as error:
        my_logger.error(f'Ошибка при извлечении пользователей в базе данных {error}')
