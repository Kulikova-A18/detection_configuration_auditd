import os
import subprocess
import sys
from audit_rule import AuditRule

class FileAccessRule(AuditRule):
    """Класс для правил аудита доступа к файлам."""
    def __init__(self, path, permissions, key):
        super().__init__(key)
        self.path = path
        self.permissions = permissions

    def validate(self):
        if not os.path.exists(self.path):
            print(f"Ошибка: Путь '{self.path}' не существует.")
            sys.exit(1)
        if not isinstance(self.permissions, list) or not all(p in {"r", "w", "x"} for p in self.permissions):
            print(f"Ошибка: Некорректные права доступа для '{self.path}'.")
            sys.exit(1)

    def set_rule(self):
        permissions_string = ''.join(self.permissions)
        command = f"auditctl -w {self.path} -p {permissions_string} -k {self.key}"
        subprocess.run(command, shell=True, check=True)
        print(f"Установлено правило: {command}")
