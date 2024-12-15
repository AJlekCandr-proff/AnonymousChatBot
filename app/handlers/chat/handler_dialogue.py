from aiogram import Router
from aiogram.types import Message

from app.filters.filters_chat import MessagesFilter, CharFilter
from app.config.settings import anonymous_bot


router = Router(name=__name__)


@router.message(CharFilter(), MessagesFilter())
async def handler_messages_dialog(message: Message, companion_id: int) -> None:
    """
    Асинхронный обработчик сообщений пользователей, которые разговаривают с кем-либо.
    Пересылает сообщения собеседнику.

    :param message: Объект класса Message.
    :param companion_id: ID собеседника.
    """

    await anonymous_bot.send_message(chat_id=companion_id, text=message.text)
