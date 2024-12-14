from sqlalchemy import select

from app.validation.model_dialog import Dialog
from app.config.settings import async_session, my_logger
from ..models.dialog import Chats


async def select_dialogs() -> list[Dialog]:
    """
    Асинхронная функция для извлечения всех ведущихся диалогов из данных.

    :return: Список объектов класса Dialog.
    """

    try:
        async with async_session() as session:
            query = select(Chats)

            result = await session.execute(query)

            list_dialogs = result.scalars().all()

            return list_dialogs

    except Exception as error:
        my_logger.error(error)
