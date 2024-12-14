from aiogram.filters import Filter
from aiogram.types import Message

from app.database.CRUDs.select_dialog import select_dialog


class StartSearchFilter(Filter):
    async def __call__(self, message: Message) -> Message | None:
        """
        Асинхронный фильтр нажатия кнопки "🚀 Поиск случайного собеседника".

        :param message: Объект класса Message.
        :return: Объект класса Message, либо None.
        """

        if message.text == '🚀 Поиск случайного собеседника':
            return message


class ChatFilter(Filter):
    async def __call__(self, message: Message) -> dict[str, int] | None:
        """
        Асинхронный фильтр сообщений пользователя, которые состоят в диалоге с кем-либо.

        :param message: Объект класса Message.

        :return: ID собеседника (аргумент для обработчика), либо None.
        """

        user_id = message.from_user.id
        current_dialog = await select_dialog(user_id)

        if current_dialog:
            companion: int = current_dialog.user_2 ^ current_dialog.user_1 ^ user_id

            return {'companion': companion}
