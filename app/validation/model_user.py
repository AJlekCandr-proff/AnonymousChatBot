from datetime import datetime

from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    telegram_id: PositiveInt
    full_name: str
    date: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
