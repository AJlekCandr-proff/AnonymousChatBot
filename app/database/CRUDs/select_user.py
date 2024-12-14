from sqlalchemy import select

from app.database.models.dialog import Chats
from app.validation.model_user import User
from app.config.settings import async_session, my_logger


async def select_user(user_id: int) -> User | None:
    """
    Асинхронная функция для проверки, состоит ли пользователь в диалоге с кем-либо.

    :param user_id: Telegram ID пользователя.

    :return: Объект класса User.
    """

    try:
        async with async_session() as session:
            query = select(Chats).where(Chats.user_1 == user_id or Chats.user_2 == user_id)

            result = await session.execute(query)

            user = result.scalar()

            return user

    except Exception as e:
        my_logger.info(f'Ошибка при извлечении пользователя {user_id}: {e}')
