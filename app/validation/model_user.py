from datetime import datetime

from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    telegram_id: PositiveInt
    fullname: str
    date: datetime
