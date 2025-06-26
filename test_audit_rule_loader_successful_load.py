import unittest
from audit_rule_loader import AuditRuleLoader

class TestAuditRuleLoader(unittest.TestCase):
    def test_successful_load(self):
        loader = AuditRuleLoader('test_audit_rules.yaml')
        rules = loader.load_audit_rules()
        
        self.assertIsInstance(rules, list)
        self.assertGreater(len(rules), 0)  # Проверяем, что правила загружены

if __name__ == '__main__':
    unittest.main()
