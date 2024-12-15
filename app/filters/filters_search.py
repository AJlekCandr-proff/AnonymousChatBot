from aiogram.types import Message
from aiogram.filters import Filter


class InterestsFilters(Filter):
    async def __call__(self, message: Message) -> Message | None:
        """
        Асинхронный фильтр нажатия кнопки "📖 Интересы поиска".

        :param message: Объект класса Message.

        :return: Объект класса Message, либо None.
        """

        if message.text == '📖 Интересы поиска':
            return message
