from asyncpg import UniqueViolationError

from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError

from app.config.settings import my_logger, async_session
from ..models.dialog import Chats


async def add_new_dialog(companions: tuple[int, int]) -> None:
    """
    Асинхронная функция добавления нового диалога в анонимном чате.

    :param companions: ID обоих собеседников.
    """

    try:
        async with async_session() as session:
            query = insert(Chats).values(user_1=companions[0], user_2=companions[1])

            await session.execute(query)

            await session.commit()

            return my_logger.info(f'Новый диалог между {companions[0]} и {companions[1]} пользователями Telegram!')

    except (IntegrityError, UniqueViolationError):
        my_logger.error(f'Ошибка уникальности диалога: Пользователь уже состоит в диалоге!')

