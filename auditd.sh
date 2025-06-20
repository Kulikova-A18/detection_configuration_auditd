#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Пожалуйста, запустите этот скрипт с правами суперпользователя"
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "--- Установка зависимостей ---"

if [ -f "$SCRIPT_DIR/install_requirements.sh" ]; then
    bash "$SCRIPT_DIR/install_requirements.sh" || echo "Пропуск установки зависимостей"
else
    echo "Файл install_requirements.sh не найден"
fi

echo "--- Создание правил ---"

python3 "$SCRIPT_DIR/main.py" || echo "Пропуск запуска auditd"

# # echo "--- Создание правил ---"

# sudo systemctl restart auditd || echo "Пропуск запуска auditd"

echo "--- Список созданных правил ---"

auditctl -l

exit 0
