from aiogram import Router

from .commands import router as router_commands


router = Router(name=__name__)


router.include_routers(router_commands)
