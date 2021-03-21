
class Point:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def __str__(self):
        return f'[{self.x_coord}, {self.y_coord}]'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x_coord == other.x_coord and self.y_coord == other.y_coord
        else:
            return False

    def __copy__(self):
        return Point(self.x_coord, self.y_coord)
