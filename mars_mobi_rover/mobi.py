# -*- coding=utf-8 -*-
"""Mobi Space Administration module
"""

import mars


class OutOfBoundsException(Exception):
    pass


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
        """Truns rover left
        """

        direction_index = mars.DIRECTIONS.index(
            self.current_coordinate.heading
        )
        new_direction_index = (
            direction_index - 1) % len(mars.DIRECTIONS)
        self.current_coordinate.heading = mars.DIRECTIONS[new_direction_index]

    def turn_right(self):
        """Truns rover right
        """
        direction_index = mars.DIRECTIONS.index(
            self.current_coordinate.heading
        )
        new_direction_index = (
            direction_index + 1) % len(mars.DIRECTIONS)
        self.current_coordinate.heading = mars.DIRECTIONS[new_direction_index]

    def move_forward(self, bounderies=None):
        """Move rover forward on Coordinate heading

        Keyword Arguments:
            bounderies {Bounderies} -- Bounderies of an Plateau
            (default: {None})
        """

        heading = self.current_coordinate.heading
        new_location = mars.Coordinate(
            self.current_coordinate.x,
            self.current_coordinate.y,
            self.current_coordinate.heading
        )
        if heading == 'N':
            new_location.y += 1
        elif heading == 'S':
            new_location.y -= 1
        elif heading == 'W':
            new_location.x -= 1
        elif heading == 'E':
            new_location.x += 1

        if bounderies is not None:
            if isinstance(bounderies, mars.Bounderies):
                if bounderies.check_move(new_location):
                    self.current_coordinate = new_location
                else:
                    raise OutOfBoundsException(
                        'Rover {0} out of bounderies'.format(self.name)
                    )
            else:
                raise TypeError(
                    'A Bounderies object was expected. Received {0}'.format(
                        type(bounderies)
                    )
                )
        else:
            self.current_coordinate = new_location

    def execute_instructions(self, instruction_set, bounderies=None):
        """Execute the instruction set on current rover

        Arguments:
            instruction_set {String} -- Instruction set string.
            Must contain only L, R or M letters.
            L: turns rover left
            R: turns rover right
            M: move rover forward
        """
        for command in instruction_set:
            if command in ['L', 'M', 'R']:
                if command == 'L':
                    self.turn_left()
                elif command == 'R':
                    self.turn_right()
                else:
                    try:
                        self.move_forward(bounderies)
                    except OutOfBoundsException:
                        pass
