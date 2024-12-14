from sqlalchemy import delete

from app.config.settings import async_session, my_logger
from app.database.models.users import SearchCompanion


async def delete_user_in_search(user_id: int) -> None:
    """
    Асинхронная функция удаления пользователя из таблицы поиска собеседника.

    :param user_id: ID пользователя.
    """

    try:
        async with async_session() as session:
            query = delete(SearchCompanion).where(SearchCompanion.telegram_id == user_id)

            await session.execute(query)

            await session.commit()

    except Exception as error:
        my_logger.error(f'Произошла ошибка во время удаления пользователя из таблицы поиска собеседника: {error}')
