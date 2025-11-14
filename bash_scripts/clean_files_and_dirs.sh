#!/bin/bash
# Удаление кэшированных файлов и директорий для backend на python


for dir in $(find . -type d -name "__pycache__"); do 
		sudo rm -rf "$dir"; 
done

rm -rf backend/.coverage 2>/dev/null || true
rm -rf backend/.pytest_cache 2>/dev/null || true