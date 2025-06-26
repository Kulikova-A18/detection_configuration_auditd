import subprocess
import sys
from audit_rule import AuditRule

class ProcessAuditRule(AuditRule):
    """Класс для правил аудита процессов."""
    def __init__(self, command, action, key):
        super().__init__(key)
        self.command = command
        self.action = action

    def validate(self):
        if not self.command or not isinstance(self.command, str):
            print("Ошибка: Команда не указана или некорректна.")
            sys.exit(1)
        if not self.action or not isinstance(self.action, str):
            print("Ошибка: Действие не указано или некорректно.")
            sys.exit(1)

    def set_rule(self):
        command = f"auditctl -a {self.action} -S {self.command} -k {self.key}"
        subprocess.run(command, shell=True, check=True)
        print(f"Установлено правило: {command}")
