# -*- coding=utf-8 -*-
"""Unit test module for Rovers"""

from unittest import TestCase

from mars_mobi_rover.mars import Coordinate, boundaries
from mars_mobi_rover.mobi import OutOfBoundsException, Rover


class TestRovers(TestCase):
    """Unit test case for `mars_mobi_rover.mobi.Rover` class"""

    def setUp(self):
        """setup common objects for unit tests"""
        self.rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'N'))

    def tearDown(self):
        del self.rover1

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

    def test_y_coordinate_move(self):
        """Test Y coordinate movement"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'N'))
        rover1.move_forward()
        self.assertEquals(rover1.current_coordinate.y, 1)
        rover1.turn_left()
        rover1.turn_left()
        rover1.move_forward()
        self.assertEquals(rover1.current_coordinate.y, 0)

    def test_x_coordinate_move(self):
        """Test X coordinate movement"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'E'))
        rover1.move_forward()
        self.assertEquals(rover1.current_coordinate.x, 1)
        rover1.turn_left()
        rover1.turn_left()
        rover1.move_forward()
        self.assertEquals(rover1.current_coordinate.x, 0)

    def test_y_coordinate_move_with_boundaries(self):
        """Test Y coordinate movement with boundaries"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'N'))
        bound = boundaries(5, 5)
        rover1.move_forward(bound)
        self.assertEquals(rover1.current_coordinate.y, 1)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        self.assertEquals(rover1.current_coordinate.y, 5)
        rover1.turn_left()
        rover1.turn_left()
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        self.assertEquals(rover1.current_coordinate.y, 0)

    def test_x_coordinate_move_with_boundaries(self):
        """Test X coordinate movement with boundaries"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'E'))
        bound = boundaries(5, 5)
        rover1.move_forward(bound)
        self.assertEquals(rover1.current_coordinate.x, 1)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        self.assertEquals(rover1.current_coordinate.x, 5)
        rover1.turn_left()
        rover1.turn_left()
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        rover1.move_forward(bound)
        self.assertEquals(rover1.current_coordinate.x, 0)

    def test_fail_top_bound(self):
        """Test move forward fail top bound"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'S'))
        bound = boundaries(5, 5)
        with self.assertRaises(OutOfBoundsException):
            rover1.move_forward(bound)

    def test_fail_botton_bound(self):
        """Test move forward fail botton bound"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 5, 'N'))
        bound = boundaries(5, 5)
        with self.assertRaises(OutOfBoundsException):
            rover1.move_forward(bound)

    def test_fail_left_bound(self):
        """Test move forward fail left bound"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'W'))
        bound = boundaries(5, 5)
        with self.assertRaises(OutOfBoundsException):
            rover1.move_forward(bound)

    def test_fail_right_bound(self):
        """Test move forward fail right bound"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(5, 0, 'E'))
        bound = boundaries(5, 5)
        with self.assertRaises(OutOfBoundsException):
            rover1.move_forward(bound)

    def test_rover_instructions(self):
        """Test rover instruction set execution"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'N'))
        bound = boundaries(5, 5)
        instruction_set = "MMRMMLMLMLM"
        # Excepect coordinate 1, 2 S
        rover1.execute_instructions(instruction_set, bound)
        self.assertEqual(rover1.current_coordinate, Coordinate(1, 2, 'S'))

    def test_rover_instructions_out_of_bounds(self):
        """Test rover instruction set execution with OutOfBounds"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'N'))
        bound = boundaries(5, 5)
        instruction_set = "MMMMMMMRMMRMM"
        # Excepect coordinate 1, 2 S
        rover1.execute_instructions(instruction_set, bound)
        self.assertEqual(rover1.current_coordinate, Coordinate(2, 3, 'S'))

    def test_rover_instruction_bad_bounds(self):
        """Test rover instruction set execution with bad bounds"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'N'))
        bound = float(9)
        instruction_set = "MMRMMLMLMLM"
        with self.assertRaises(TypeError):
            rover1.execute_instructions(instruction_set, bound)

    def test_rover_object_ne(self):
        """Test not Equal operator for Rover Class"""

        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'N'))
        rover2 = Rover(
            name="Rover2", landing_coordinate=Coordinate(0, 0, 'N'))
        self.assertEqual(self.rover1, rover1)
        self.assertNotEqual(self.rover1, rover2)

    def test_rover_string(self):
        """Test string representation of a Rover object"""
        rover1 = Rover(
            name="Rover1", landing_coordinate=Coordinate(0, 0, 'N'))
        self.assertEqual(rover1.__str__(), "Rover1:0 0 N")
