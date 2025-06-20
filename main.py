import yaml
import subprocess
import os
import sys

def load_audit_rules_from_yaml(yaml_file_path):
    """Загружает правила аудита из YAML-файла."""
    try:
        with open(yaml_file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{yaml_file_path}' не найден.")
        sys.exit(1)
    except yaml.YAMLError as yaml_error:
        print(f"Ошибка при загрузке YAML-файла: {yaml_error}")
        sys.exit(1)

def validate_audit_rules(audit_rules):
    """Валидация правил аудита."""
    valid_permissions_set = {"r", "w", "x", "a"}
    
    try:
        for audit_rule in audit_rules['audit_rules']:
            rule_path = audit_rule.get('path')
            rule_permissions = audit_rule.get('permissions')

            validate_rule_path(rule_path)
            validate_rule_existence(rule_path)
            validate_rule_type(rule_path)
            validate_rule_permissions(rule_permissions, valid_permissions_set, rule_path)
    except Exception as validation_error:
        print(f"Ошибка при валидации правил: {validation_error}")
        sys.exit(1)

def validate_rule_path(rule_path):
    """Проверка на наличие пути."""
    if not rule_path:
        print("Ошибка: Путь не указан.")
        sys.exit(1)

def validate_rule_existence(rule_path):
    """Проверка, существует ли файл или директория."""
    if not os.path.exists(rule_path):
        print(f"Ошибка: Указанный путь '{rule_path}' не существует.")
        sys.exit(1)

def validate_rule_type(rule_path):
    """Проверка, является ли путь файлом или директорией."""
    if not (os.path.isfile(rule_path) or os.path.isdir(rule_path)):
        print(f"Ошибка: '{rule_path}' не является файлом или директорией.")
        sys.exit(1)

def validate_rule_permissions(rule_permissions, valid_permissions_set, rule_path):
    """Проверка прав доступа."""
    if rule_permissions is None or not isinstance(rule_permissions, list):
        print(f"Ошибка: Права доступа для '{rule_path}' не указаны или некорректны.")
        sys.exit(1)

    for permission in rule_permissions:
        if permission not in valid_permissions_set:
            print(f"Ошибка: Некорректное право доступа '{permission}' для '{rule_path}'.")
            sys.exit(1)

def set_audit_rules(audit_rules):
    """Устанавливает правила аудита с помощью команды auditctl."""
    for audit_rule in audit_rules['audit_rules']:
        rule_path = audit_rule['path']
        rule_permissions_string = ''.join(audit_rule['permissions']) 
        command_to_execute = f"auditctl -w {rule_path} -p {rule_permissions_string}"
        
        try:
            subprocess.run(command_to_execute, shell=True, check=True)
            print(f"Установлено правило: {command_to_execute}")
        except subprocess.CalledProcessError as command_error:
            print(f"Ошибка при установке правила: {command_error}")

if __name__ == "__main__":
    yaml_file_path = 'audit_rules.yaml'
    audit_rules = load_audit_rules_from_yaml(yaml_file_path)
    
    # Проверяем правила перед установкой
    validate_audit_rules(audit_rules)
    
    # Устанавливаем правила аудита
    set_audit_rules(audit_rules)
