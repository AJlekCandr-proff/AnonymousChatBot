from sqlalchemy import insert

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
