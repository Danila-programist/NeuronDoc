"""Тестирование файла main.py"""

import pytest

from httpx import AsyncClient


@pytest.mark.asyncio
class TestMain:
    """Тестирование ручек, которые идут из коробки в FastAPI"""
    async def test_invalid_endpoint_returns_404(self, client: AsyncClient):
        """Проверка несуществующей ручки"""
        response = await client.get("/nonexistent-endpoint")
        assert response.status_code == 404

    async def test_docs_available(self, client: AsyncClient):
        """Проверка существующей ручки /docs"""
        response = await client.get("/docs")
        assert response.status_code == 200

    async def test_openapi_available(self, client: AsyncClient):
        """Проверка существующей ручки /openapi.json"""
        response = await client.get("/openapi.json")
        assert response.status_code == 200

    async def test_redoc_available(self, client: AsyncClient):
        """Проверка существующей ручки /redoc"""
        response = await client.get("/redoc")
        assert response.status_code == 200
