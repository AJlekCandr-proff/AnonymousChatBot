from aiogram import Router
from aiogram.types import Message

from app.filters.filters_chat import MessagesFilter, ChatFilter
from app.config.settings import anonymous_bot


router = Router(name=__name__)


@router.message(ChatFilter(), MessagesFilter())
async def handler_messages_dialog(message: Message, companion_id: int) -> None:
    """
    Асинхронный обработчик сообщений пользователей, которые разговаривают с кем-либо.
    Пересылает сообщения собеседнику.

    :param message: Объект класса Message.
    :param companion_id: ID собеседника.
    """

    if message.caption or message.text:
        if message.video:
            await anonymous_bot.send_video(chat_id=companion_id, video=message.video.file_id, caption=message.caption)

        if message.photo:
            await anonymous_bot.send_photo(chat_id=companion_id, photo=message.photo[-1].file_id, caption=message.caption)

        else:
            await anonymous_bot.send_message(chat_id=companion_id, text=message.text)

    elif message.video:
        await anonymous_bot.send_video(chat_id=companion_id, video=message.video.file_id, caption=message.caption)

    elif message.photo:
        await anonymous_bot.send_photo(chat_id=companion_id, photo=message.photo[-1].file_id)

    elif message.voice:
        await anonymous_bot.send_voice_note(chat_id=companion_id, voice=message.voice.file_id)

    elif message.video_note:
        await anonymous_bot.send_video_note(chat_id=companion_id, video_note=message.video_note.file_id)
