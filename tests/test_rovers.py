# -*- coding=utf-8 -*-
"""Unit test module for Rovers"""

from unittest import TestCase

from mars_mobi_rover.mars import Coordinate
from mars_mobi_rover.mobi import Rover


class TestRovers(TestCase):
    """Unit test case for `mars_mobi_rover.mobi.Rover` class"""

    def setUp(self):
        """setup common objects for unit tests"""
        self.rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'N'))

    def test_rover_object(self):
        """Test Rover Class"""
        self.assertEqual(self.rover1.name, 'Rover1')
        self.assertEqual(self.rover1.current_coordinate, Coordinate(0, 0, 'N'))

    def test_turn_right(self):
        """Test Rover Turn Right operation"""
        self.rover1.turn_right()
        self.assertEqual(self.rover1.current_coordinate.heading, 'E')
        self.rover1.turn_right()
        self.assertEqual(self.rover1.current_coordinate.heading, 'S')
        self.rover1.turn_right()
        self.assertEqual(self.rover1.current_coordinate.heading, 'W')

    def test_turn_left(self):
        """Test Rover Turn Left operation"""
        self.rover1.turn_left()
        self.assertEqual(self.rover1.current_coordinate.heading, 'W')
        self.rover1.turn_left()
        self.assertEqual(self.rover1.current_coordinate.heading, 'S')
        self.rover1.turn_left()
        self.assertEqual(self.rover1.current_coordinate.heading, 'E')

    # def test_x_coordinate_move(self):
    #     """Test X coordinate movement"""
    #     self.fail()

    # def test_y_coordinate_move(self):
    #     """Test Y coordinate movement"""
    #     self.fail()
