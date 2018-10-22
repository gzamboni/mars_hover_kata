#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `mars_mobi_rover` package."""


from unittest import TestCase
from click.testing import CliRunner
from mars_mobi_rover import cli


class TestCli(TestCase):
    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        self.assertEqual(result.exit_code, 0)
        help_result = runner.invoke(cli.main, ['--help'])
        self.assertEqual(help_result.exit_code, 0)
        self.assertIn('--help  Show this message and exit.',
                      help_result.output)

    def test_command_line_mission(self):
        """Test running a mission from std input"""
        stdin_text = """Plateau:5 5
Rover1 Landing:1 2 N
Rover1 Instructions:LMLMLMLMM
Rover2 Landing:3 3 E
Rover2 Instructions:MMRMMRMRRM"""
        expected_result = """Rover1:1 3 N
Rover2:5 1 E

"""
        runner = CliRunner()
        result = runner.invoke(cli.main, input=stdin_text)
        self.assertFalse(result.exception)
        self.assertEqual(result.output, expected_result)
