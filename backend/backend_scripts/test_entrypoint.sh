#!/bin/bash
# Выполнение миграций и запуск тестового приложения

poetry run alembic upgrade head
exec poetry run pytest -vv