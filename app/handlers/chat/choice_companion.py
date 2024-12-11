import random

from app.validation.model_user import User
from app.database.CRUDs.select_users import selects_users


async def choice_companion(user_id: int) -> tuple[User, User]:
    """
    Асинхронная функция для реализации выборки случайного собеседника.

    :param user_id: ID пользователя.

    :return: Кортеж из двух пользователей диалога.
    """

    dialog = [user_id]

    users = await selects_users()

    while len(users) > 0:
        if len(users) > 1:
            companion = random.choice(users)

            return dialog.append(companion)
