#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"


check_pip() {
    if command -v pip &> /dev/null; then
        echo "pip уже установлен."
        return 0
    else
        echo "pip не установлен."
        return 1
    fi
}

install_pip() {
    read -p "pip не установлен. Хотите установить его? (y/n): " answer
    if [[ "$answer" == "y" || "$answer" == "" ]]; then
        echo "Устанавливаем pip..."

        sudo apt-get update
        sudo apt-get install -y python3-pip
    else
        echo "pip не будет установлен. Завершение работы."
        exit 1
    fi
}

if ! check_pip; then
    install_pip
fi


pip install -r ${SCRIPT_DIR}/requirements.txt
