from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.config.settings import views
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
