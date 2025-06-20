import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import sys
import yaml

from audit import (
    load_audit_rules_from_yaml,
    validate_audit_rules,
    validate_rule_path,
    validate_rule_existence,
    validate_rule_type,
    validate_rule_permissions,
    set_audit_rules
)

class TestAuditFunctions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data=yaml.dump({'audit_rules': [{'path': '/tmp/testfile', 'permissions': ['r', 'w']}] }))
    def test_load_audit_rules_from_yaml_success(self, mock_file):
        rules = load_audit_rules_from_yaml('fake_path.yaml')
        self.assertEqual(len(rules['audit_rules']), 1)
        self.assertEqual(rules['audit_rules'][0]['path'], '/tmp/testfile')

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_audit_rules_from_yaml_file_not_found(self, mock_file):
        with self.assertRaises(SystemExit):
            load_audit_rules_from_yaml('fake_path.yaml')

    @patch("builtins.open", side_effect=yaml.YAMLError("YAML error"))
    def test_load_audit_rules_from_yaml_yaml_error(self, mock_file):
        with self.assertRaises(SystemExit):
            load_audit_rules_from_yaml('fake_path.yaml')

    def test_validate_rule_path_empty(self):
        with self.assertRaises(SystemExit):
            validate_rule_path("")

    @patch("os.path.exists", return_value=False)
    def test_validate_rule_existence_not_exists(self, mock_exists):
        with self.assertRaises(SystemExit):
            validate_rule_existence('/fake/path')

    @patch("os.path.isfile", return_value=False)
    @patch("os.path.isdir", return_value=False)
    def test_validate_rule_type_invalid(self, mock_isdir, mock_isfile):
        with self.assertRaises(SystemExit):
            validate_rule_type('/fake/path')

    def test_validate_rule_permissions_none(self):
        with self.assertRaises(SystemExit):
            validate_rule_permissions(None, {"r", "w", "x", "a"}, '/fake/path')

    def test_validate_rule_permissions_invalid_type(self):
        with self.assertRaises(SystemExit):
            validate_rule_permissions("invalid", {"r", "w", "x", "a"}, '/fake/path')

    def test_validate_rule_permissions_invalid_permission(self):
        with self.assertRaises(SystemExit):
            validate_rule_permissions(['r', 'invalid'], {"r", "w", "x", "a"}, '/fake/path')

    @patch("subprocess.run")
    def test_set_audit_rules_success(self, mock_run):
        mock_run.return_value = MagicMock()
        audit_rules = {'audit_rules': [{'path': '/tmp/testfile', 'permissions': ['r', 'w']}]}
        set_audit_rules(audit_rules)
        mock_run.assert_called_once_with('auditctl -w /tmp/testfile -p rw', shell=True, check=True)

    @patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, 'command'))
    def test_set_audit_rules_command_error(self, mock_run):
        audit_rules = {'audit_rules': [{'path': '/tmp/testfile', 'permissions': ['r', 'w']}]}
        with self.assertRaises(SystemExit):
            set_audit_rules(audit_rules)

    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", return_value=True)
    @patch("os.path.isdir", return_value=False)
    def test_validate_rule_type_file(self, mock_isdir, mock_isfile):
        try:
            validate_rule_type('/fake/file')
        except SystemExit:
            self.fail("validate_rule_type raised SystemExit unexpectedly!")

    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", return_value=False)
    @patch("os.path.isdir", return_value=True)
    def test_validate_rule_type_directory(self, mock_isdir, mock_isfile):
        try:
            validate_rule_type('/fake/dir')
        except SystemExit:
            self.fail("validate_rule_type raised SystemExit unexpectedly!")

if __name__ == '__main__':
    unittest.main()
