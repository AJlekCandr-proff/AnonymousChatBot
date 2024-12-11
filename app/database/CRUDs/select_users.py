from sqlalchemy import select

from app.database.models.users import SearchCompanion
from app.validation.model_user import User
from app.config.settings import async_session, my_logger


async def selects_users() -> list[User]:
    try:
        async with async_session() as session:
            query = select(SearchCompanion)

            list_users_in_search = await session.execute(query)

            return list_users_in_search.all()

    except Exception as error:
        my_logger.error(f'Ошибка при извлечении пользователей в базе данных {error}')


