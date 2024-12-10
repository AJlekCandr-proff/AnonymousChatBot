from aiogram.filters import Filter
from aiogram.types import Message


class StartSearchFilter(Filter):
    async def __call__(self, message: Message) -> Message | None:
        """
        Асинхронный фильтр нажатия кнопки "🚀 Поиск случайного собеседника".

        :param message: Объект класса Message.
        :return : Объект класса Message, либо None.
        """

        if message.text == '🚀 Поиск случайного собеседника':
            return message
