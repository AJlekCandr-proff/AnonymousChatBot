from aiogram.filters import Filter
from aiogram.types import Message

from app.database.CRUDs.select_dialogue import select_dialog
from app.database.CRUDs.select_users import selects_user


class StartSearchFilter(Filter):
    async def __call__(self, message: Message) -> Message | None:
        """
        Асинхронный фильтр нажатия кнопки "🚀 Поиск случайного собеседника".

        :param message: Объект класса Message.
        :return: Объект класса Message, либо None.
        """

        if message.text == '🚀 Поиск случайного собеседника':
            return message


class StopChatFilter(Filter):
    async def __call__(self, message: Message) -> Message | None:
        """
        Асинхронный фильтр нажатия кнопки завершения диалога "Стоп ❌".

        :param message: Объект класса Message.

        :return: Объект класса Message, либо None.
        """

        if message.text == 'Стоп ❌':
            return message


class SearchFilter(Filter):
    async def __call__(self, message: Message) -> Message | None:
        """
        Асинхронный фильтр для проверки пользователя на состояние поиска собеседника.

        :param message: Объект класса Message.

        :return: Объект класса Message, либо None.
        """

        if await selects_user(message.from_user.id) is None:
            return message


class CharFilter(Filter):
    async def __call__(self, message: Message) -> dict[str, int] | None:
        """
        Асинхронный фильтр сообщений пользователя, которые состоят в диалоге с кем-либо.

        :param message: Объект класса Message.

        :return: Объект класса Message, либо None.
        """

        if await select_dialog(message.from_user.id):
            return message


class MessagesFilter(Filter):
    async def __call__(self, message: Message) -> dict[str, int] | None:
        """
        Асинхронный фильтр сообщений пользователя, которые состоят в диалоге с кем-либо.

        :param message: Объект класса Message.

        :return: ID собеседника (аргумент для обработчика), либо None.
        """

        user_id = message.from_user.id
        current_dialog = await select_dialog(user_id)

        companion: int = current_dialog.user_2 ^ current_dialog.user_1 ^ user_id

        return {'companion_id': companion}
