#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Пожалуйста, запустите этот скрипт с правами суперпользователя"
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for test_file in "$SCRIPT_DIR"/*.py; do
    echo "Запуск тестов в файле: $test_file"
    python3 -m unittest "$test_file"
    echo "-----------------------------------"
done

exit 0
