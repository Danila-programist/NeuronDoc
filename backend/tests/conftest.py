"""Инициализация начальных значений и параметров для тестирования функциональности приложения"""

from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from main import app


@pytest_asyncio.fixture(scope="function")
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Создание пустого клиента"""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as async_client:
        yield async_client
