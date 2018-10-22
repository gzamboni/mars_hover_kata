#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `mars_mobi_rover` package."""


from unittest import TestCase

from mars_mobi_rover.mars import Coordinate, Plateau, Rover
from mars_mobi_rover.parser import InputParser


class TestMarsMobiRover(TestCase):
    """UnitTest for Mobi Rover Parser module

    Arguments:
        TestCase {TestCase} -- Base class for UnitTest
    """

    def setUp(self):
        """Hook method for setting up the test fixture before exercising it."""
        self.stdin_text = """Plateau:5 5
Rover1 Landing:1 2 N
Rover1 Instructions:LMLMLMLMM
Rover2 Landing:3 3 E
Rover2 Instructions:MMRMMRMRRM"""
        self.fail_rover_text = """Plateau:5 5
Rover1 Landing:1 2 2 N
Rover1 Instructions:12313131
Rover2 Landing:3 3 E
Rover2 Instructions:MMRMMRMRRM"""
        self.random_data = "dwiopfhjiodsjiofeij"

    def tearDown(self):
        """Hook method for deconstructing the test fixture after testing it."""
        pass

    def test_stdin_plateau_parser(self):
        parser = InputParser(self.stdin_text)
        self.assertEqual(parser._input_instructions, self.stdin_text)
        plateau = parser.get_plateau()
        self.assertIsInstance(plateau, Plateau)
        self.assertEqual(plateau.boundaries.x_min, 0)
        self.assertEqual(plateau.boundaries.x_max, 5)
        self.assertEqual(plateau.boundaries.y_min, 0)
        self.assertEqual(plateau.boundaries.y_max, 5)

    def test_stdin_parser_fail(self):
        """Test for no Plateau configuration on input"""
        parser = InputParser(self.random_data)
        with self.assertRaises(ValueError):
            parser.get_plateau()

    def test_rover_landing_parser(self):
        """Test Rover landing parser method"""
        expected_list = [
            Rover("Rover1", Coordinate(1, 2, 'N')),
            Rover("Rover2", Coordinate(3, 3, 'E'))
        ]
        parser = InputParser(self.stdin_text)
        rover_list = parser.get_rover_list()
        self.assertEqual(
            rover_list, expected_list
        )

    def test_rover_landing_parser_fail(self):
        """Test for failed Rover landing parser method"""
        parser = InputParser(self.fail_rover_text)
        with self.assertRaises(ValueError):
            parser.get_rover_list()

    def test_rover_landing_parser_no_data(self):
        """Test for no data for Rover landing parser method"""
        parser = InputParser(self.random_data)
        with self.assertRaises(ValueError):
            parser.get_rover_list()
        parser = InputParser("")
        with self.assertRaises(ValueError):
            parser.get_rover_list()

    def test_mission_instructions_parser(self):
        """Test mission instructions parser method"""
        expected_mission = {
            "Rover1": "LMLMLMLMM",
            "Rover2": "MMRMMRMRRM"
        }
        parser = InputParser(self.stdin_text)
        mission_instructions = parser.get_mission_instructions()
        self.assertEqual(
            mission_instructions, expected_mission
        )

    def test_mission_instructions_parser_fail(self):
        """Test for failed mission instructions parser method"""
        parser = InputParser(self.fail_rover_text)
        with self.assertRaises(ValueError):
            parser.get_mission_instructions()

    def test_mission_instructions_parser_no_data(self):
        """Test for no data for mission instructions parser method"""
        parser = InputParser(self.random_data)
        with self.assertRaises(ValueError):
            parser.get_mission_instructions()
        parser = InputParser("")
        with self.assertRaises(ValueError):
            parser.get_mission_instructions()
