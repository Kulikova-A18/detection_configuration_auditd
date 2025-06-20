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
    @patch("os.path.exists", return_value=False)
    def test_validate_rule_existence_not_exist(self, mock_exists):
        with self.assertRaises(SystemExit):
            validate_rule_existence('/non/existent/path')

if __name__ == "__main__":
    unittest.main()
