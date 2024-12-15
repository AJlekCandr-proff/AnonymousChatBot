from aiogram import Router
from aiogram.types import Message

from app.filters.filters_search import InterestsFilters


router = Router(name=__name__)


@router.message(InterestsFilters())
async def handler_interests(message: Message) -> None:
    """
    Асинхронный обработчик нажатия кнопки "📖 Интересы поиска".
    Присылает меню для выбора интересов поиска.

    :param message: Объект класса Message.
    """

    pass
