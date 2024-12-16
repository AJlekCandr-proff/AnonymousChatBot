from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.database.CRUDs.add_user import add_new_user
from app.database.CRUDs.select_users import select_user
from app.validation.model_user import User
from app.config.settings import views, my_logger
from app.keyboards.menu_keyboards import start_menu


router = Router(name=__name__)


@router.message(CommandStart())
async def handler_start(message: Message) -> None:
    """
    Асинхронный обработчик команды /start.
    Присылает приветственное сообщение для пользователя.

    :param message: Объект класса Message.
    """

    await message.answer(text=views.get('start_msg'), reply_markup=start_menu())

    if await select_user(message.from_user.id) is None:
        try:
            new_user = User(telegram_id=message.from_user.id, full_name=message.from_user.full_name)

        except ValueError:
            return my_logger.error(f'Что-то пошло не так при добавлении нового пользователя {message.from_user.id}')

        await add_new_user(new_user)
