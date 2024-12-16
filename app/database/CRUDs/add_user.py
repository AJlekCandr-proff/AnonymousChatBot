from sqlalchemy import insert, update

from app.validation.model_user import User
from app.database.models.users import Profiles
from app.config.settings import async_session, my_logger


async def add_new_user(user: User) -> None:
    """
    Асинхронная функция регистрации пользователя в базе данных.

    :param user: Объект класса User.
    """

    try:
        async with async_session() as session:
            query = insert(Profiles).values(User.model_dump())

            await session.execute(query)

            await session.commit()

            return my_logger.info(f'Пользователь {user.telegram_id} был добавлен в базу данных!')

    except Exception as error:
        my_logger.error(f'При регистрации пользователя возникла ошибка: {error}')


async def add_user_in_search(user: User) -> None:
    """
    Асинхронная функция добавления пользователя в поиск собеседника.

    :param user: Объект класса User.
    """

    try:
        async with async_session() as session:
            query = update(Profiles).values(in_search=True).where(Profiles.telegram_id == user.telegram_id)

            await session.execute(query)

            await session.commit()

            return my_logger.info(f'Пользователь {user.telegram_id} начал поиск собеседника...')

    except Exception as error:
        my_logger.error(f'При начале поиска собеседника возникла ошибка: {error}')
