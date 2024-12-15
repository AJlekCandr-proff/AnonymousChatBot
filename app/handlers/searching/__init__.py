from aiogram import Router

from .handler_interests import router as router_interests


router = Router(name=__name__)


router.include_routers(router_interests)
