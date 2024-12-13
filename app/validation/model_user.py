from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    telegram_id: PositiveInt
    full_name: str
