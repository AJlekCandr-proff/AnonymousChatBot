import asyncio

from aiogram import Bot, Dispatcher

from app import router as root_router
from app.config.settings import anonymous_bot, my_logger


async def start(bot: Bot) -> None:
    """
    Асинхронная функция для запуска всей программы.

    :param bot: Объект класса Bot.
    """

    dp = Dispatcher()
    dp.include_router(root_router)

    my_logger.info('Bot successfully started!')

    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start(anonymous_bot))
