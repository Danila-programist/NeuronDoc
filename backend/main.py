"""Точка входа Backend приложения"""

import uvicorn
from fastapi import FastAPI

from app.utils import logger


app = FastAPI(
    title="Анализатор текста",
    description="API для работы с проектом NeuronDoc",
    version="1.0.0",
)


if __name__ == "__main__":
    logger.info("Инициализация работы приложения FastAPI")
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)
    logger.info("Завершение работы приложения FastAPI")
