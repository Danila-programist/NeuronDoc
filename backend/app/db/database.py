"""Файл для получении сессии с базой данных"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core import settings


engine = create_async_engine(settings.ASYNC_DATABASE_DSN)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Генерация новой сессии"""
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
