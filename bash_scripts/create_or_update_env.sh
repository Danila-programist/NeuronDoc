#!/bin/bash
# Создаёт или обновляет .env из .env.example

if [ ! -f .env ]; then
    cp .env.example .env
elif ! cmp -s .env .env.example; then
    cp .env.example .env
fi