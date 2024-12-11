from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.filters.filters_chat import StartSearchFilter
from app.config.settings import views, my_logger, anonymous_bot
from app.database.CRUDs.insert_user import add_user
from app.validation.model_user import User
from .choice_companion import choice_companion


router = Router(name=__name__)


@router.message(StartSearchFilter())
async def handler_start_search(message: Message) -> None:
    """
    Обработчик нажатия кнопки "🚀 Поиск случайного собеседника".
     Поиск собеседника и начинает диалог.

    :param message: Объект класса Message.
    :param state: Объект класса FSMContext.
    """

    try:
        user = User(telegram_id=message.from_user.id, full_name=message.from_user.full_name)

    except ValueError:
        return my_logger.error(f'Ошибка валидации, при добавлении пользователя {message.from_user.id}')

    await add_user(user)

    await message.answer(text=views.get('search_msg'))

    dialog_companions = await choice_companion(message, user)

    for companion in dialog_companions:
        await anonymous_bot.send_message(chat_id=companion.telegram_id, text=views.get('start_chat'))
