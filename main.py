from audit_rule_loader import AuditRuleLoader

# 1. audit_rule.py — базовый класс AuditRule.
# 2. ssh_login_rule.py — класс SSHLoginRule.
# 3. file_access_rule.py — класс FileAccessRule.
# 4. package_installation_rule.py — класс PackageInstallationRule.
# 5. process_audit_rule.py — класс ProcessAuditRule.
# 6. audit_rule_loader.py — класс для загрузки правил из YAML-файла.

def main():
    yaml_file_path = 'audit_rules.yaml'
    
    # Загружаем правила
    loader = AuditRuleLoader(yaml_file_path)
    
    # Проверяем и устанавливаем правила
    for rule in loader.rules:
        rule.validate()
        rule.set_rule()

if __name__ == "__main__":
    main()
