"""Инициализация базового класса длял работы с Alembic"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Класс, который будет для всех остальных классов из models"""
