from aiogram import Router

from .handler_search import router as router_search
from .handler_dialogue import router as router_messages
from .handler_stop import router as router_stop_dialogue


router = Router(name=__name__)


router.include_routers(router_search, router_stop_dialogue, router_messages)
