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
    @patch("os.path.isfile", return_value=False)
    @patch("os.path.isdir", return_value=False)
    def test_validate_rule_type_invalid(self, mock_isdir, mock_isfile):
        with self.assertRaises(SystemExit):
            validate_rule_type('/invalid/path')

if __name__ == "__main__":
    unittest.main()
