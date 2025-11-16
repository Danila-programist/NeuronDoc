#!/bin/bash
# Выполнение миграций и запуск приложения

poetry run alembic upgrade head
exec poetry run python3.12 main.py