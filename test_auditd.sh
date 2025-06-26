#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Пожалуйста, запустите этот скрипт с правами суперпользователя"
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

total_tests=0
total_failures=0

for test_file in "$SCRIPT_DIR"/test_*.py; do
    echo "Запуск тестов в файле: $test_file"
    
    python3 -m unittest "$test_file"

    if [ $? -ne 0 ]; then
        total_failures=$((total_failures + 1))
    fi
    
    total_tests=$((total_tests + 1))

    echo "$result"
    echo "-----------------------------------"
done

echo "Всего тестов: $total_tests"
echo "Неудачных тестов: $total_failures"
echo "Успешных тестов: $((total_tests - total_failures))"
