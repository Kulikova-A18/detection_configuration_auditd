import unittest
from audit_rule_loader import AuditRuleLoader

class TestAuditRuleLoaderInvalidRuleType(unittest.TestCase):
    def test_invalid_rule_type(self):
        loader = AuditRuleLoader('test_invalid_rule_type.yaml')
        rules = loader.load_audit_rules()
        
        self.assertEqual(len(rules), 0)

if __name__ == '__main__':
    unittest.main()
