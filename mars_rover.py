from enum import Enum
import re

class MarsMission:
    def __init__(self, input):
        # Create a `MarsRover` object for every two input lines.
        self._mars_rovers = [ MarsRover((int(x), int(y)), dir, instr) for x, y, dir, instr
                              in re.findall(r'(\d+) (\d+) ([NESW])\n([LRM]+)', input) ]
    
    def execute_instructions(self):
        """
        Method to execute the instruction for all the given `MarsRover` objects.
        """
        for mars_rover in self._mars_rovers:
            mars_rover.perform_instructions()
        
        # Return the string representations of all `MarsRover` objects, separated by newlines.
        return '\n'.join([ str(x) for x in self._mars_rovers])

class Direction(Enum):
    """
    Direction enum, represented as their movement values.
    """
    N = (0,1)
    E = (1,0)
    S = (0,-1)
    W = (-1,0)

    def __str__(self):
        return self.name

class MarsRover:
    def __init__(self, position, direction, instructions):
        self._position = position
        self._direction = Direction[direction]
        self._instructions = instructions

    def __str__(self):
        return f'{self._position[0]} {self._position[1]} {self._direction}'
        
    def _move(self):
        """
        Method to add the direction value to the current position.
        """
        self._position = tuple(sum(x) for x in zip(self._position, self._direction.value))
    
    def _update_direction(self, rotation):
        """
        Method to update the direction of a `MarsRover`.
        """
        match self._direction:
            case Direction.N: self._direction = Direction.E if rotation == 'R' else Direction.W
            case Direction.E: self._direction = Direction.S if rotation == 'R' else Direction.N
            case Direction.S: self._direction = Direction.W if rotation == 'R' else Direction.E
            case Direction.W: self._direction = Direction.N if rotation == 'R' else Direction.S
    
    def perform_instructions(self):
        """
        Method to perform all instructions of a `MarsRover`.
        """
        for instruction in self._instructions:
            if instruction == 'M':
                self._move()
            else:
                self._update_direction(instruction)