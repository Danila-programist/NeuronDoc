"""Тесты для конфигурационного файла settings.py"""

import pytest

from app.core import settings, Settings


class TestSettings:
    """Тестирование конфигурационного файла settings.py"""

    def test_settings_attributes(self):
        """Проверка наличия атрибутов в классе Settings с их типами"""
        assert hasattr(settings, "DB_NAME")
        assert hasattr(settings, "DB_USER")
        assert hasattr(settings, "DB_PASSWORD")
        assert hasattr(settings, "DB_HOST")
        assert hasattr(settings, "DB_CONTAINER_NAME")
        assert hasattr(settings, "DB_PORT")
        assert isinstance(settings.DB_PORT, int)
        assert isinstance(settings.DB_NAME, str)
        assert isinstance(settings.DB_USER, str)
        assert isinstance(settings.DB_PASSWORD, str)
        assert isinstance(settings.DB_HOST, str)

    def test_async_database_dsn_property(self):
        """Проверка корректности свойства ASYNC_DATABASE_DSN"""
        dsn = settings.ASYNC_DATABASE_DSN
        assert dsn.startswith("postgresql+asyncpg://")

    def test_invalid_db_port(self):
        """Проверка ошибки при неверном типе DB_PORT"""
        with pytest.raises(ValueError):
            Settings(
                DB_NAME="test_db",
                DB_USER="test_user",
                DB_PASSWORD="test_password",
                DB_HOST="localhost",
                DB_PORT="not_an_int",
            )

    def test_invalid_name_number_types(self):
        """Проверка ошибки при неверном типе DB_NAME"""
        with pytest.raises(ValueError):
            Settings(
                DB_NAME=12345,
                DB_USER="test_user",
                DB_PASSWORD="test_password",
                DB_HOST="localhost",
                DB_PORT=5432,
            )

    def test_invalid_user_number_types(self):
        """Проверка ошибки при неверном типе DB_USER"""
        with pytest.raises(ValueError):
            Settings(
                DB_NAME="test_db",
                DB_USER=67890,
                DB_PASSWORD="test_password",
                DB_HOST="localhost",
                DB_PORT=5432,
            )

    def test_invalid_password_number_types(self):
        """Проверка ошибки при неверном типе DB_PASSWORD"""
        with pytest.raises(ValueError):
            Settings(
                DB_NAME="test_db",
                DB_USER="test_user",
                DB_PASSWORD=13579,
                DB_HOST="localhost",
                DB_PORT=5432,
            )

    def test_invalid_host_number_types(self):
        """Проверка ошибки при неверном типе DB_HOST"""
        with pytest.raises(ValueError):
            Settings(
                DB_NAME="test_db",
                DB_USER="test_user",
                DB_PASSWORD="test_password",
                DB_HOST=24680,
                DB_PORT=5432,
            )
 
    

    
