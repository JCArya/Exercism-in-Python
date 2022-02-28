
"""exercism robot simulator module."""
# Globals for the directions
# Change the values as you see fit
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'
class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        """
        Initialize a robot at specific coordinates and facing a specified direction.
 
        :param str direction - The direction to face (WEST, NORTH, EAST, SOUTH).
        :param int x - The x coordinate for the robot.
        :param int y - The y coordinate for the robot.
        """
        self.DIRECTION_SEQUENCE = [WEST, NORTH, EAST, SOUTH]
        self.direction = direction
        self.coordinates = (x, y)
    def move(self, instructions:str):
        """
        Have the robot perform a sequence of movements.
 
        :param instructions str - The sequence of movements to perform
 
        Calls _move for each movement.
        """
        for instruction in instructions:
            self._move(instruction)
    def _rotate_right(self):
        index = self.DIRECTION_SEQUENCE.index(self.direction)
        if index == len(self.DIRECTION_SEQUENCE) - 1:
            self.direction = self.DIRECTION_SEQUENCE[0]
        else:
            self.direction = self.DIRECTION_SEQUENCE[index + 1]
    def _rotate_left(self):
        index = self.DIRECTION_SEQUENCE.index(self.direction)
        if index == 0:
            self.direction = self.DIRECTION_SEQUENCE[-1]
        else:
            self.direction = self.DIRECTION_SEQUENCE[index - 1]
    def _move(self, instruction:str):
        if instruction == "R":
            self._rotate_right()
        elif instruction == "L":
            self._rotate_left()
        elif instruction == "A":
            x, y = self.coordinates
            if self.direction == EAST:
                x += 1
            elif self.direction == NORTH:
                y += 1
            elif self.direction == WEST:
                x -= 1
            else: # SOUTH
                y -= 1
            self.coordinates = (x, y)
        else:
            raise ValueError(f"Bad instruction: {instruction}")