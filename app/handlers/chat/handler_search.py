from aiogram import Router
from aiogram.types import Message

from app.filters.filters_chat import StartSearchFilter
from app.config.settings import views, my_logger
from app.database.CRUDs.insert_user import add_user
from app.validation.model_user import User
from .choice_companion import choice_companion


router = Router(name=__name__)


@router.message(StartSearchFilter())
async def handler_start_search(message: Message) -> None:
    """
    Обработчик нажатия кнопки "🚀 Поиск случайного собеседника".

    :param message: Объект класса Message,
    """

    try:
        await add_user(User(telegram_id=message.from_user.id, full_name=message.from_user.full_name))

    except ValueError:
        return my_logger.error(f'Ошибка валидации, при добавлении пользователя {message.from_user.id}')

    await message.answer(text=views.get('search_msg'))

    await choice_companion(message.from_user.id)
