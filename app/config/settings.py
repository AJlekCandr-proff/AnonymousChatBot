from pydantic import SecretStr

from loguru import logger

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn

from ..utils.read_yaml import read_views


class Settings(BaseSettings):
    telegram_api_token: SecretStr
    data_base_url: PostgresDsn

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()

my_logger = logger

anonymous_bot = Bot(token=settings.telegram_api_token.get_secret_value(), default=DefaultBotProperties(parse_mode='HTML'))

views = read_views()
