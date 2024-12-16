import asyncio

import random

from aiogram.types import Message

from app.validation.model_user import User
from app.database.CRUDs.select_users import select_users
from app.database.CRUDs.select_dialogue import select_dialog
from app.config.settings import my_logger, views


async def choice_companion(message: Message, user: User) -> tuple[User, User]:
    """
    Асинхронная функция для реализации выборки случайного собеседника.

    :param user: Профиль пользователя.
    :param message: Объект класса Message.

    :return: Кортеж из двух пользователей диалога.
    """

    dialog = [user]

    users = await select_users()

    await message.answer(text=views.get('error_search')) if len(users) > 1 else None

    while len(users) > 0:
        if len(users) > 1:
            companion: User = random.choice(users)

            if companion.telegram_id != user.telegram_id:
                dialog.append(companion)

                my_logger.info(f'Нашлись 2 собеседника для диалога: {[companion.telegram_id, user.telegram_id]}')

                return dialog

            else:
                my_logger.info(f'По случайности с пользователем {user.telegram_id} произошла ошибка в поиске!')

        else:
            if await select_dialog(user.telegram_id):
                return

            await asyncio.sleep(5)

            my_logger.info('Недостаточно пользователей в базе данных, повторный поиск...')
