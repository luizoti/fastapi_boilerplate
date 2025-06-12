import os
import typing

from alembic.config import Config
from pydantic_settings import BaseSettings

from app.core import BASE_DIR

ALEMBIC_CFG = Config(os.path.join(BASE_DIR, "alembic.ini"))


class Settings(BaseSettings):
    SECRET_KEY: typing.Text = None

    SQLALCHEMY_DATABASE_URI: typing.Text = ALEMBIC_CFG.get_main_option("sqlalchemy.url")
    ALGORITHM: typing.Text = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        extra = "allow"
        env_file = str(BASE_DIR / ".env")
        env_file_encoding = "utf-8"

    def model_dump(self, *args, **kwargs) -> dict[str, typing.Any]:
        """Turn .env settings uppercase over pydantic Settings."""
        return {x.upper(): y for x, y in super().model_dump(*args, **kwargs).items()}


SETTINGS = Settings().model_dump()
