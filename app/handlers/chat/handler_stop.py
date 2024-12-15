from aiogram import Router
from aiogram.types import Message

from app.filters.filters_chat import StopChatFilter, ChatFilter
from app.database.CRUDs.delete_dialogue import delete_dialogue
from app.database.CRUDs.select_dialogue import select_dialog
from app.config.settings import anonymous_bot
from app.keyboards.menu_keyboards import start_menu


router = Router(name=__name__)


@router.message(StopChatFilter(), ChatFilter())
async def handler_stop_dialogue(message: Message) -> None:
    """
    Асинхронный обработчик нажатия кнопки "Стоп ❌".

    :param message: Объект класса Message.
    """

    user_id = message.from_user.id

    current_dialog = await select_dialog(user_id)

    await delete_dialogue(user_id)

    for user_id in [current_dialog.user_1, current_dialog.user_2]:
        await anonymous_bot.send_message(
            chat_id=user_id,
            text='❗️<b>Диалог завершен</b>\n\n',
                 # f'Вы отправили <ins>{}</ins> сообщений! 💬\n\n',
            reply_markup=start_menu(),
        )
