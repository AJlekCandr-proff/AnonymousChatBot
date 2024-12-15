from sqlalchemy import delete, or_

from app.config.settings import async_session, my_logger
from ..models.chat import Chats


async def delete_dialogue(user_id: int) -> None:
    """
    Асинхронная функция удаления диалога из таблицы действующих диалогов.

    :param user_id: Telegram ID пользователя, который решил прекратить диалог.
    """

    try:
        async with async_session() as session:
            query = delete(Chats).where(or_(Chats.user_1 == user_id, Chats.user_2 == user_id))

            await session.execute(query)

            await session.commit()

    except Exception as error:
        my_logger.error(f'При прекращении и удалении диалога возникла ошибка: {error}')
