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

    def __init__(self, x, y, heading, *args, **kwargs):
        self.x = x
        self.y = y
        self._heading = heading

    def __eq__(a, b):
        return (
            (a.x == b.x) and
            (a.y == b.y) and
            (a._heading == b._heading)
        )

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


class Bounderies(object):
    """Class to handle bounderies on Mars Plateaus
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


class Plateau(object):
    """Class to represent a Plateau in Mars"""

    _rovers = []

    def __init__(self, max_x, max_y, *args, **kwargs):
        self._bounderies = Bounderies(max_x, max_y)

    @property
    def rovers(self):
        return self._rovers

    def add_rover(self, rover):
        """Add a rover object to this Plateau"""
        if isinstance(rover, Rover):
            if self.get_rover(rover.name) is None:
                self._rovers.append(rover)
            else:
                raise ValueError('Duplicated rover')
        else:
            raise TypeError('Only Rover objects can be added to Plateau Class')

    @property
    def bounderies(self):
        """Return the plateau bounderies object"""
        return self._bounderies

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
