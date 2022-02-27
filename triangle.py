def equilateral(sides):
    return (sides[0] == sides[1] == sides[2]) and sides[0] != 0
def isosceles(sides):
    for side in sides:
        if side == 0:
            return false
    if sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[2] + sides[1] < sides[0]:
            return False
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[2] == sides[1]
def scalene(sides):
    for side in sides:
        if side == 0:
            return false
    if sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[2] + sides[1] < sides[0]:
            return False
    return (sides[0] != sides[1] != sides[2])