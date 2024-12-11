import random

from app.validation.model_user import User
from app.database.CRUDs.select_users import selects_users


async def choice_companion(user: User) -> tuple[User, User]:
    """
    Асинхронная функция для реализации выборки случайного собеседника.

    :param user: ID пользователя.

    :return: Кортеж из двух пользователей диалога.
    """

    dialog = [user]

    users = await selects_users()

    while len(users) > 0:
        if len(users) > 1:
            companion = random.choice(users)

            return dialog.append(companion)
