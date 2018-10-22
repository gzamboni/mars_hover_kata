# -*- coding=utf-8 -*-
"""Parser module for command line utils"""

import re

from mars_mobi_rover.mars import Coordinate, Plateau, Rover


class InputParser(object):
    """
    Provides utils to parse mars rover instructions
    Input:

    Configuration Input: The first line of input is the upper-right coordinates
    of the plateau, the lower-left coordinates are assumed to be 0,0.

    Per Rover Input:

    Input 1: Landing co-ordinates for the named Rover. The position is made up
    of two integers and a letter separated by spaces, corresponding to the
    x and y co-ordinates and the rover's orientation.

    Input 2: Navigation instructions for the named rover. i.e a string
    containing ('L', 'R', 'M').

    Ex.:

    Plateau:5 5
    Rover1 Landing:1 2 N
    Rover1 Instructions:LMLMLMLMM
    Rover2 Landing:3 3 E
    Rover2 Instructions:MMRMMRMRRM
    """

    def __init__(self, stdin_text):
        if stdin_text:
            self._input_instructions = stdin_text
            self._lines = self._input_instructions.splitlines()

    def get_plateau(self):
        """Returns a Plateau object with data from input text

        Returns:
            Plateau: Plateau object from input text
        """
        if len(self._lines) > 0:
            plateau_data = re.match(r"Plateau\:(\d+)\s(\d+)\n*",
                                    self._lines[0])
            if plateau_data:
                x = int(float(plateau_data.group(1)))
                y = int(float(plateau_data.group(2)))
                new_plateau = Plateau(x, y)
                return new_plateau
            else:
                raise ValueError(
                    "No Plateau description was found on input data")

    def get_rover_list(self):
        """Return a list with all Rovers objects parsed from input text

        Returns:
            List of Rover -- A list of all rover object found on input data
        """
        if len(self._lines) > 0:
            rover_list = []
            landing_lines = [line for line in self._lines if "Landing" in line]
            if len(landing_lines) > 0:
                for line in landing_lines:
                    rover_data = re.match(
                        r"(\w+)\sLanding:(\d+)\s(\d+)\s(N|S|E|W)\n*",
                        line
                    )
                    if rover_data and len(rover_data.groups()) == 4:
                        new_rover = Rover(
                            rover_data.group(1),
                            Coordinate(
                                int(float(rover_data.group(2))),
                                int(float(rover_data.group(3))),
                                rover_data.group(4)
                            )
                        )
                        rover_list.append(new_rover)
                    else:
                        raise ValueError(
                            "No Rover Landing data was found on input data"
                        )
                return rover_list
            else:
                raise ValueError(
                    "No Rover Landing data was found on input data"
                )
        else:
            raise ValueError(
                "No Rover Landing data was found on input data"
            )

    def get_mission_instructions(self):
        """Parse all mission instructions from input data

        Returns:
            dict -- A dict objects with all rovers instructions
        """
        if len(self._lines) > 0:
            mission_instructions = {}
            landing_lines = [
                line for line in self._lines if "Instructions" in line]
            if len(landing_lines) > 0:
                for line in landing_lines:
                    instruc_data = re.match(
                        r"(\w+)\sInstructions:([L|R|M]+)",
                        line
                    )
                    if instruc_data and len(instruc_data.groups()) == 2:
                        mission_instructions.update(
                            {
                                instruc_data.group(1): instruc_data.group(2)
                            }
                        )
                    else:
                        raise ValueError(
                            "No Rover instructions was found on input data"
                        )
                return mission_instructions
            else:
                raise ValueError(
                    "No Rover instructions was found on input data"
                )
        else:
            raise ValueError(
                "No Rover instructions was found on input data"
            )
