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

    @patch("subprocess.run")
    def test_set_audit_rules_success(self, mock_run):
        audit_rules = {'audit_rules': [{'path': '/some/path', 'permissions': ['r', 'w']}]}
        set_audit_rules(audit_rules)
        mock_run.assert_called_once_with('auditctl -w /some/path -p rw', shell=True, check=True)


if __name__ == "__main__":
    unittest.main()
