from sqlalchemy import select

from app.validation.model_dialog import Dialog
from app.validation.model_user import User
from app.config.settings import async_session, my_logger
from ..models.dialog import Chats


async def select_dialog(user_id: int) -> tuple[User, User] | None:
    """
    Асинхронная функция проверки пользователя на ведение диалога с кем-либо.

    :return: Кортеж из двух объектов User.
    """

    try:
        async with async_session() as session:
            query = select(Chats).where(Chats.user_1 == user_id or Chats.user_2 == user_id)

            result = await session.execute(query)

            current_dialog: Dialog = result.scalar()

            return tuple[current_dialog.user_1, current_dialog.user_2]

    except Exception as error:
        my_logger.error(f'При проверке пользователя на ведение диалоге с кем-либо возникла ошибка: {error}')
