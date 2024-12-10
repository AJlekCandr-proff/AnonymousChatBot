from aiogram import Router
from aiogram.types import Message

from app.filters.filters_chat import StartSearchFilter
from app.config.settings import views


router = Router(name=__name__)


@router.message(StartSearchFilter())
async def handler_start_search(message: Message) -> None:
    """
    Обработчик нажатия кнопки "🚀 Поиск случайного собеседника".

    :param message: Объект класса Message,
    """

    await message.answer(text=views.get('search_msg'))
