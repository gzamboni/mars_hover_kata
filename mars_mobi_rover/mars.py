# -*- coding: utf-8 -*-

"""Mars module."""

from mars_mobi_rover.mobi import Rover


DIRECTIONS = [
    "N",
    "E",
    "S",
    "W"
]


class Coordinate(object):
    """Describe a position and heading on Mars Surface"""

    def __init__(self, x, y, heading):
        self._x = x
        self._y = y
        self._heading = heading

    def __eq__(self, other):
        """Equal operator for Coordinate class"""
        return (
            (self._x == other._x) and
            (self._y == other._y) and
            (self._heading == other._heading)
        )

    def __ne__(self, other):
        """Not equal operator for Coordinate class"""
        return not self.__eq__(other)

    def __str__(self):
        return "{0} {1} {2}".format(
            self._x, self._y, self._heading
        )

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def heading(self):
        """Getter for heading property"""
        return self._heading

    @heading.setter
    def heading(self, value):
        if value in DIRECTIONS:
            self._heading = value
        else:
            raise ValueError('Invalid Mars heading')


class boundaries(object):
    """Class to handle boundaries on Mars Plateaus
    """

    def __init__(self, x, y, *args, **kwargs):
        self.x_min = 0
        self.y_min = 0
        self.x_max = x
        self.y_max = y

    def check_move(self, new_location):
        """Check if the object can move to the new_location

        Arguments:
            new_location {Coordinate} -- The Coordinate object that represents
            the new object location

        Returns:
            Boolean -- True: new location is valid, False: new location is
            invalid
        """
        return (
            (self.x_min <= new_location.x <= self.x_max) and
            (self.y_min <= new_location.y <= self.y_max)
        )

    def __eq__(self, other):
        """Equal operator for boundaries Class"""
        return (
            (self.x_min == other.x_min) and
            (self.y_min == other.y_min) and
            (self.x_max == other.x_max) and
            (self.y_max == other.y_max)
        )

    def __ne__(self, other):
        """Not equal operator for boundaries Class"""
        return not self.__eq__(other)


class Plateau(object):
    """Class to represent a Plateau in Mars"""

    def __init__(self, max_x, max_y, *args, **kwargs):
        self._boundaries = boundaries(max_x, max_y)
        self._rovers = []

    @property
    def rovers(self):
        return self._rovers

    def add_rover(self, rover):
        """Add a rover object to this Plateau"""
        if isinstance(rover, Rover):
            if self.get_rover(rover.name) is None:
                self._rovers.append(rover)
        else:
            raise TypeError('Only Rover objects can be added to Plateau Class')

    @property
    def boundaries(self):
        """Return the plateau boundaries object"""
        return self._boundaries

    def get_rover(self, rover_name):
        """Return a rover object by name

        Arguments:
            rover_name {str} -- Rover Name
        """
        ret_value = None
        try:
            ret_value = next(
                item for item in self._rovers if item.name == rover_name
            )
        except StopIteration:
            ret_value = None
        return ret_value

    def __eq__(self, other):
        """Plateau equals operator"""
        return (
            (self.boundaries == other.boundaries)
        )

    def __ne__(self, other):
        """Plateau not equals operator"""
        return not self.__eq__(other)
