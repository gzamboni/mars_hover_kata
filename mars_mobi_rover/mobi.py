# -*- coding=utf-8 -*-
"""Mobi Space Administration module
"""

import mars


class Rover(object):
    """Mars Rover class
    """

    def __init__(self, name, landing_coordinate, *args, **kwargs):
        self.name = name
        self.current_coordinate = landing_coordinate

    def __eq__(a, b):
        """Equals operator"""
        return (
            (a.name == b.name) and
            (a.current_coordinate == b.current_coordinate)
        )

    def turn_left(self):
        direction_index = mars.DIRECTIONS.index(
            self.current_coordinate.heading
        )
        new_direction_index = (
            direction_index - 1) % len(mars.DIRECTIONS)
        self.current_coordinate.heading = mars.DIRECTIONS[new_direction_index]

    def turn_right(self):
        direction_index = mars.DIRECTIONS.index(
            self.current_coordinate.heading
        )
        new_direction_index = (
            direction_index + 1) % len(mars.DIRECTIONS)
        self.current_coordinate.heading = mars.DIRECTIONS[new_direction_index]
