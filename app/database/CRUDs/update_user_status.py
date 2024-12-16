from sqlalchemy import update

from app.config.settings import async_session, my_logger
from app.database.models import Profiles


async def update_user_status(user_id: int, in_search_state: bool) -> None:
    """
    Асинхронная функция добавления пользователя в поиск собеседника.

    :param user_id: Объект класса User.
    :param in_search_state: Константа True или False.
    """

    try:
        async with async_session() as session:
            query = update(Profiles).values(in_search=in_search_state).where(Profiles.telegram_id == user_id)

            await session.execute(query)

            await session.commit()

            return my_logger.info(f'Пользователь {user_id} начал поиск собеседника...')

    except Exception as error:
        my_logger.error(f'При начале поиска собеседника возникла ошибка: {error}')
