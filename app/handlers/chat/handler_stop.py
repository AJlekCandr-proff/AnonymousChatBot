from aiogram import Router
from aiogram.types import Message

from app.filters.filters_chat import StopChatFilter


router = Router(name=__name__)


@router.message(StopChatFilter())
async def handler_stop_dialogue(message: Message) -> None:
    """
    Асинхронный обработчик нажатия кнопки "Стоп ❌".

    :param message: Объект класса Message.
    """
