from aiogram import Router
from aiogram.types import Message

from app.filters.filters_chat import StartSearchFilter, SearchFilter
from app.config.settings import views, anonymous_bot
from app.keyboards.menu_keyboards import chat_menu
from app.database.CRUDs.select_users import select_user
from app.database.CRUDs.update_user_status import update_user_status
from app.database.CRUDs.add_new_dialogue import add_new_dialog
from app.utils.choice_companion import choice_companion


router = Router(name=__name__)


@router.message(StartSearchFilter(), SearchFilter())
async def handler_start_search(message: Message) -> None:
    """
    Обработчик нажатия кнопки "🚀 Поиск случайного собеседника".
     Поиск собеседника и начинает диалог.

    :param message: Объект класса Message.
    """

    current_user_id = message.from_user.id
    user = await select_user(current_user_id)

    await update_user_status(current_user_id, True)

    await message.answer(text=views.get('search_msg'))

    dialog_companions = await choice_companion(message, user)

    await add_new_dialog(dialog_companions)

    for companion in dialog_companions:
        await update_user_status(current_user_id, False)

        await anonymous_bot.send_message(
            chat_id=companion.telegram_id,
            text=views.get('start_chat'),
            reply_markup=chat_menu()
        )
