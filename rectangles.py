
from typing import Iterable
def rectangles(strings: Iterable[str]) -> int:
    """Count the number of valid rectangles in a diagram
 
    :param strings: Iterable[str] - collection of ascii strings representing a diagram
    :return: int - number of valid rectangles which are in the diagram
    """
    verticies = []
    for i, row in enumerate(strings):
        for j, point in enumerate(row):
            if point == "+":
                verticies.append((i, j))
    if not verticies:
        return 0
    width, height = len(strings[0]), len(strings)
    rectangles = set()
    for corner in verticies:
        for row in range(0, height - corner[0] + 1):
            for col in range(0, width - corner[1] + 1):
                right_point = (corner[0], corner[1] + col)
                down_point = (corner[0] + row, corner[1])
                oppposing_point = (corner[0] + row, corner[1] + col)
                if (right_point in verticies and down_point in verticies and oppposing_point in verticies) and (
                    len(set((corner, right_point, down_point, oppposing_point))) == 4
                ):
                    top = all(strings[corner[0]][x] in "+-" for x in range(corner[1], corner[1] + col))
                    left = all(strings[x][corner[1]] in "+|" for x in range(corner[0], corner[0] + row))
                    bottom = all(strings[corner[0] + row][x] in "+-" for x in range(corner[1], corner[1] + col))
                    right = all(strings[x][corner[1] + col] in "+|" for x in range(corner[0], corner[0] + row))
                    if top and left and bottom and right:
                        rectangles.add((corner, right_point, down_point, oppposing_point))
    return len(rectangles)
