# -*- coding: utf-8 -*-

"""Mars Mission module."""

from mars_mobi_rover.parser import InputParser


class Mission(object):
    """Class to execute the mars rover mission"""

    def __init__(self, input_data, *args, **kwargs):
        self._input_data = input_data
        _parser = InputParser(self._input_data)
        self._plateau = _parser.get_plateau()
        for _rover in _parser.get_rover_list():
            self._plateau.add_rover(_rover)
        self._instructions = _parser.get_mission_instructions()

    def execute(self):
        """Execute all rover instructions on deployed rovers"""
        result = ""
        for rover in self._plateau.rovers:
            instruction = self._instructions.get(rover.name, None)
            if instruction:
                rover.execute_instructions(
                    instruction, self._plateau.boundaries
                )
                result += "{0}\n".format(rover)
        return result
