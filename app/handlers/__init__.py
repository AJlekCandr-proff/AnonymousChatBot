from aiogram import Router

from .commands import router as router_commands
from .chat import router as router_chat
from .searching import router as router_search


router = Router(name=__name__)


router.include_routers(router_commands, router_chat, router_search)
