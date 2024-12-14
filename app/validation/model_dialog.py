from pydantic import BaseModel, PositiveInt


class Dialog(BaseModel):
    user_1: PositiveInt
    user_2: PositiveInt
    messages: PositiveInt
