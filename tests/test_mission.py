# -*- coding: utf-8 -*-

"""Mars Mission test module."""

from unittest import TestCase

from mars_mobi_rover.mars import Plateau, Rover, Coordinate
from mars_mobi_rover.mission import Mission


class TestMission(TestCase):
    """Unit test case for Mission Class"""

    def setUp(self):
        self.stdin_text = """Plateau:5 5
Rover1 Landing:1 2 N
Rover1 Instructions:LMLMLMLMM
Rover2 Landing:3 3 E
Rover2 Instructions:MMRMMRMRRM"""
        self.expected_list = [
            Rover("Rover1", Coordinate(1, 2, 'N')),
            Rover("Rover2", Coordinate(3, 3, 'E'))
        ]
        self.mission = Mission(self.stdin_text)

    def test_mission_setup(self):
        self.assertEqual(Plateau(5, 5), self.mission._plateau)
        self.assertEqual(self.expected_list, self.mission._plateau.rovers)
        expected_mission = {
            "Rover1": "LMLMLMLMM",
            "Rover2": "MMRMMRMRRM"
        }
        self.assertEqual(
            self.mission._instructions, expected_mission
        )

    def test_mission_execution(self):
        expected_result = """Rover1:1 3 N
Rover2:5 1 E
"""
        result = self.mission.execute()
        self.assertEqual(result, expected_result)
