#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `mars_mobi_rover` package."""

import pytest

from unittest import TestCase

from click.testing import CliRunner

from mars_mobi_rover import mars_mobi_rover
from mars_mobi_rover import cli


class TestMarsMobiRover(TestCase):
    """UnitTest for Mobi Rover

    Arguments:
        TestCase {TestCase} -- Base class for UnitTest
    """

    def setUp(self):
        """Hook method for setting up the test fixture before exercising it."""
        pass

    def tearDown(self):
        """Hook method for deconstructing the test fixture after testing it."""
        pass

    def testCli(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        self.assertEqual(result.exit_code, 0)
        self.assertIn('mars_mobi_rover.cli.main', result.output)
        help_result = runner.invoke(cli.main, ['--help'])
        self.assertEqual(help_result.exit_code, 0)
        self.assertIn('--help  Show this message and exit.',
                      help_result.output)
