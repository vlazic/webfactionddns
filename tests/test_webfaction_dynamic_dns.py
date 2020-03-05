#!/usr/bin/env python

"""Tests for `webfaction_dynamic_dns` package."""


import unittest
from click.testing import CliRunner

from webfaction_dynamic_dns import webfaction_dynamic_dns
from webfaction_dynamic_dns import cli


class TestWebfaction_dynamic_dns(unittest.TestCase):
    """Tests for `webfaction_dynamic_dns` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'webfaction_dynamic_dns.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
