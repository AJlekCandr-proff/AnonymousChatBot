from sqlalchemy import select

from app.config.settings import async_session, my_logger
from ..models.chat import Chats


async def select_dialog(user_id: int) -> Chats | None:
    """
    Асинхронная функция проверки пользователя на ведение диалога с кем-либо.

    :return: Объект класса Dialog.
    """

    try:
        async with async_session() as session:
            query = select(Chats).where(Chats.user_1 == user_id or Chats.user_2 == user_id)

            result = await session.execute(query)

            current_dialog = result.scalar()

            return current_dialog

    except Exception as error:
        my_logger.error(f'При проверке пользователя на ведение диалоге с кем-либо возникла ошибка: {error}')
