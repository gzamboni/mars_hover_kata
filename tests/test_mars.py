# -*- coding: utf-8 -*-

"""Tests for `mars_mobi_rover` package."""

from unittest import TestCase

from mars_mobi_rover.mars import Bounderies, Plateau, Coordinate
from mars_mobi_rover.mobi import Rover


class TestBounderies(TestCase):
    """Unit test case for Bounderies Class"""

    def setUp(self):
        self.bound = Bounderies(10, 10)

    def test_bounderies_object(self):
        """Test Bounderies Object"""
        self.assertEquals(self.bound.x_min, 0)
        self.assertEquals(self.bound.y_min, 0)
        self.assertEquals(self.bound.x_max, 10)
        self.assertEquals(self.bound.y_max, 10)

    def test_check_move(self):
        """Test check move ok"""
        new_location = Coordinate(5, 5, 'S')
        self.assertTrue(self.bound.check_move(new_location))
        new_location = Coordinate(10, 1, 'S')
        self.assertTrue(self.bound.check_move(new_location))
        new_location = Coordinate(1, 10, 'S')
        self.assertTrue(self.bound.check_move(new_location))
        new_location = Coordinate(0, 10, 'S')
        self.assertTrue(self.bound.check_move(new_location))
        new_location = Coordinate(10, 0, 'S')
        self.assertTrue(self.bound.check_move(new_location))

    def test_fail_check_move(self):
        """Test check move failed"""
        new_location = Coordinate(11, 1, 'S')
        self.assertFalse(self.bound.check_move(new_location))
        new_location = Coordinate(1, 11, 'S')
        self.assertFalse(self.bound.check_move(new_location))
        new_location = Coordinate(-1, 1, 'S')
        self.assertFalse(self.bound.check_move(new_location))
        new_location = Coordinate(1, -1, 'S')
        self.assertFalse(self.bound.check_move(new_location))


class TestCoordinate(TestCase):
    """Unit test case for Coordinate Class"""

    def test_valid_coordinate(self):
        """Test for a valid coordinate"""
        coord = Coordinate(0, 0, 'N')
        self.assertIsInstance(coord, Coordinate)
        self.assertEqual(coord.x, 0)
        self.assertEqual(coord.y, 0)
        self.assertEqual(coord.heading, 'N')

    def test_valid_headings(self):
        """Test all valid headings"""
        coord = Coordinate(0, 0, 'N')
        self.assertIsInstance(coord, Coordinate)
        self.assertEqual(coord.x, 0)
        self.assertEqual(coord.y, 0)
        self.assertEqual(coord.heading, 'N')
        coord.heading = 'E'
        self.assertEqual(coord.heading, 'E')
        coord.heading = 'S'
        self.assertEqual(coord.heading, 'S')
        coord.heading = 'W'
        self.assertEqual(coord.heading, 'W')

    def test_invalid_heading(self):
        """Test for invalid headings"""
        coord = Coordinate(0, 0, 'N')
        with self.assertRaises(ValueError):
            coord.heading = 'T'

    def test_operators(self):
        """Test Coordinate Class equals operator"""
        self.assertEqual(Coordinate(0, 0, 'N'), Coordinate(0, 0, 'N'))
        self.assertNotEqual(Coordinate(0, 0, 'N'), Coordinate(0, 1, 'N'))
        self.assertNotEqual(Coordinate(0, 0, 'N'), Coordinate(1, 0, 'N'))
        self.assertNotEqual(Coordinate(0, 0, 'N'), Coordinate(0, 0, 'S'))


class TestMarsPlateaus(TestCase):
    """Unit Tests for Mars Mission Classes
    """

    @classmethod
    def setUpClass(cls):
        """Setup common objects for TestCases
        """

        cls.Plateau = Plateau(5, 5)
        cls.new_rover1 = Rover(
            name='Rover1', landing_coordinate=Coordinate(0, 0, 'N')
        )
        cls.new_rover2 = Rover(
            name='Rover2', landing_coordinate=Coordinate(3, 3, 'S')
        )
        cls.Plateau.add_rover(cls.new_rover1)
        cls.Plateau.add_rover(cls.new_rover2)

    def test_mars_Plateau(self):
        """Test Plateau Class Constructor"""
        self.assertIsInstance(self.Plateau.bounderies, Bounderies)
        self.assertEqual(self.Plateau.bounderies.x_max, 5)
        self.assertEqual(self.Plateau.bounderies.y_max, 5)

    def test_Plateaus_rovers(self):
        """Test Rovers on Plateau"""
        self.assertIn(self.new_rover1, self.Plateau.rovers)
        self.assertIn(self.new_rover2, self.Plateau.rovers)

    def test_Plateau_get_rover(self):
        """Test Get Rover by Name"""
        filter_rover = self.Plateau.get_rover(self.new_rover1.name)
        self.assertEqual(filter_rover.name, self.new_rover1.name)
        no_result = self.Plateau.get_rover("yadayadayada")
        self.assertIsNone(no_result)

    def test_duplicate_rover_name(self):
        """Test duplicated rover"""
        new_dup_rover1 = Rover(
            name='Rover1', landing_coordinate=Coordinate(0, 0, 'N')
        )
        with self.assertRaises(ValueError):
            self.Plateau.add_rover(new_dup_rover1)

    def test_add_rover_type_error(self):
        """Test add wrong type exception"""
        with self.assertRaises(TypeError):
            self.Plateau.add_rover(object)
