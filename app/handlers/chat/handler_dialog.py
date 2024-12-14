from aiogram import Router
from aiogram.types import Message

from app.filters.filters_chat import ChatFilter
from app.config.settings import anonymous_bot


router = Router(name=__name__)


@router.message(ChatFilter())
async def handler_messages_dialog(message: Message) -> None:
    """
    Асинхронный обработчик сообщений пользователей, которые разговаривают с кем-либо.
    Пересылает сообщения собеседнику.

    :param message: Объект класса Message.
    """

    print(message.text)
