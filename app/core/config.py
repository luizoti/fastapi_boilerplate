import os
from typing import Any

from alembic.config import Config
from pydantic import AnyUrl
from pydantic_settings import BaseSettings

from app.core import BASE_DIR

ALEMBIC_CFG = Config(os.path.join(BASE_DIR, "alembic.ini"))


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: AnyUrl = ALEMBIC_CFG.get_main_option("sqlalchemy.url")

    class Config:
        extra = "allow"
        env_file = str(BASE_DIR / ".env")
        env_file_encoding = "utf-8"

    def model_dump(self, *args, **kwargs) -> dict[str, Any]:
        """Turn .env settings uppercase over pydantic Settings."""
        return {x.upper(): y for x, y in super().model_dump(*args, **kwargs).items()}


SETTINGS = Settings().model_dump()
