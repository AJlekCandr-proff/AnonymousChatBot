from datetime import datetime

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Chats(Base):
    __tablename__ = 'dialogs'

    user_1: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    user_2: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    messages: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    date: Mapped[datetime] = mapped_column(String, nullable=False, default=datetime.now())
