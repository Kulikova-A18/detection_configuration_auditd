import yaml
import sys
from ssh_login_rule import SSHLoginRule
from file_access_rule import FileAccessRule
from package_installation_rule import PackageInstallationRule
from process_audit_rule import ProcessAuditRule

class AuditRuleLoader:
    """Класс для загрузки правил аудита из YAML-файла."""
    
    def __init__(self, yaml_file_path):
        self.yaml_file_path = yaml_file_path
        self.rules = self.load_audit_rules()

    def load_audit_rules(self):
        """Загружает правила аудита из YAML-файла и создает соответствующие объекты."""
        try:
            with open(self.yaml_file_path, 'r') as file:
                data = yaml.safe_load(file)
                rules_list = []
                
                for rule_type, rules in data['audit_rules'].items():
                    for rule in rules:
                        if rule_type == 'ssh_login':
                            rules_list.append(SSHLoginRule(rule['path'], rule['permissions'], rule['key']))
                        elif rule_type == 'file_access':
                            rules_list.append(FileAccessRule(rule['path'], rule['permissions'], rule['key']))
                        elif rule_type == 'package_installation':
                            rules_list.append(PackageInstallationRule(rule['path'], rule['permissions'], rule['key']))
                        elif rule_type == 'process_audit':
                            rules_list.append(ProcessAuditRule(rule['command'], rule['action'], rule['key']))
                
                return rules_list
        except FileNotFoundError:
            print(f"Ошибка: Файл '{self.yaml_file_path}' не найден.")
            sys.exit(1)
        except yaml.YAMLError as yaml_error:
            print(f"Ошибка при загрузке YAML-файла: {yaml_error}")
            sys.exit(1)
