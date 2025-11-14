"""Инициализация объекта settings для вставки из env файла корня проекта"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    """Задаем класс Settings с атрибутами из env-файла"""

    # Database
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_CONTAINER_NAME: str
    DB_PORT: int

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def ASYNC_DATABASE_DSN(self) -> PostgresDsn:  # pylint: disable=C0103
        """Создание кастомного DSN для связи с SQLAlchemy и PostgreSQL"""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
