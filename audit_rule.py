import os
import subprocess
import sys

class AuditRule:
    """Базовый класс для правила аудита."""
    def __init__(self, key):
        self.key = key

    def validate(self):
        raise NotImplementedError("Метод validate должен быть реализован в подклассах.")

    def set_rule(self):
        raise NotImplementedError("Метод set_rule должен быть реализован в подклассах.")
