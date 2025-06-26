#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Пожалуйста, запустите этот скрипт с правами суперпользователя"
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if ! systemctl is-active --quiet auditd; then
    echo "Служба auditd не запущена или не установлена."
    read -p "Хотите установить и запустить auditd? (y/n): " answer

    if [[ "$answer" != "y" || "$answer" != "" ]]; then
        echo "Установка auditd не выполнена."
        exit 1
    fi

    echo "Установка auditd..."
    apt-get update && apt-get install -y auditd

    echo "Запуск auditd..."
    systemctl start auditd
fi

echo "--- Установка зависимостей ---"

if [ -f "$SCRIPT_DIR/install_requirements.sh" ]; then
    bash "$SCRIPT_DIR/install_requirements.sh"
else
    echo "Файл install_requirements.sh не найден"
fi

echo "--- Список текущих правил ---"
current_rules=$(auditctl -l)

if [ -n "$current_rules" ]; then
    echo "Текущие правила:"
    echo "$current_rules"
    read -p "Существуют текущие правила. Хотите перезапустить службу auditd? (y/n): " answer
    
    if [[ "$answer" == "y" || "$answer" == "" ]]; then
        echo "--- Перезапуск auditd ---"
        sudo systemctl restart auditd || echo "Не удалось перезапустить auditd"
    else
        echo "Служба auditd не будет перезапущена."
    fi
else
    echo "Текущих правил нет."
fi

echo "--- Создание правил ---"
python3 "$SCRIPT_DIR/main.py"

echo "--- Список созданных правил ---"
auditctl -l

exit 0
