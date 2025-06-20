import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import sys
import yaml
import subprocess

from main import (
    load_audit_rules_from_yaml,
    validate_audit_rules,
    validate_rule_path,
    validate_rule_existence,
    validate_rule_type,
    validate_rule_permissions,
    set_audit_rules
)


class TestAuditFunctions(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data='{"audit_rules": [{"path": "/some/path", "permissions": ["r", "w"]}]}')
    def test_load_audit_rules_from_yaml(self, mock_file):
        rules = load_audit_rules_from_yaml('dummy_path.yaml')
        self.assertEqual(len(rules['audit_rules']), 1)
        self.assertEqual(rules['audit_rules'][0]['path'], '/some/path')
        self.assertEqual(rules['audit_rules'][0]['permissions'], ['r', 'w'])

if __name__ == "__main__":
    unittest.main()
