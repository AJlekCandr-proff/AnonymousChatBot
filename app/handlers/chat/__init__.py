from aiogram import Router

from .handler_search import router as router_search


router = Router(name=__name__)


router.include_routers(router_search)
