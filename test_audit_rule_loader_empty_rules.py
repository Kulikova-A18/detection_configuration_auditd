import unittest
from audit_rule_loader import AuditRuleLoader

class TestAuditRuleLoaderEmptyRules(unittest.TestCase):
    def test_empty_rules(self):
        loader = AuditRuleLoader('test_empty_audit_rules.yaml')
        rules = loader.load_audit_rules()
        
        self.assertEqual(len(rules), 0)

if __name__ == '__main__':
    unittest.main()
