from datetime import datetime

from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    telegram_id: PositiveInt
    full_name: str
    interests: list[int] = None
    in_search: bool = False
    date: datetime = None
