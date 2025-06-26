import unittest
from audit_rule_loader import AuditRuleLoader
import sys
from unittest.mock import patch

class TestAuditRuleLoaderYamlError(unittest.TestCase):
    @patch('sys.exit')
    def test_yaml_error(self, mock_exit):
        loader = AuditRuleLoader('test_invalid_yaml.yaml')
        loader.load_audit_rules()
        mock_exit.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()
