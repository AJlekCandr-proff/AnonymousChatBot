from datetime import datetime

from sqlalchemy import String, BigInteger, DateTime, func, ARRAY, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Profiles(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    full_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=func.now())
    interests: Mapped[list] = mapped_column(ARRAY(Integer), nullable=True)
    in_search: Mapped[bool] = mapped_column(Boolean, nullable=False)
