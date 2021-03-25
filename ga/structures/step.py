import ga.structures.point as p
from ga.const import *


class Step:
    def __init__(self, ln, d):
        self.length = ln
        self.direction = d

    def __str__(self):
        dirs = ['RIGHT', 'LEFT', 'UP', 'DOWN']
        return f'[{self.length}, {dirs[self.direction]}]'

    def __eq__(self, other):
        if isinstance(other, Step):
            return self.length == other.length and self.direction == other.direction
        else:
            return False

    def __copy__(self):
        return Step(self.length, self.direction)

    def convert_to_point_list(self, start):
        return step_to_point_list(self, start)

    def set_oppose_direction(self):
        if self.direction == UP:
            self.direction = DOWN
        elif self.direction == DOWN:
            self.direction = UP
        elif self.direction == LEFT:
            self.direction = RIGHT
        elif self.direction == RIGHT:
            self.direction = LEFT
        self.length = -self.length


def step_to_point_list(step, start):
    act_point = p.Point(start.x_coord, start.y_coord)
    #p_list = [act_point]
    p_list = []

    if step.direction == RIGHT:
        for i in range(step.length):
            p_list.append(act_point)
            act_point = p.Point(act_point.x_coord + 1, act_point.y_coord)
            # p_list.append(act_point)
    elif step.direction == LEFT:
        for i in range(step.length):
            p_list.append(act_point)
            act_point = p.Point(act_point.x_coord - 1, act_point.y_coord)
            # p_list.append(act_point)
    elif step.direction == UP:
        for i in range(step.length):
            p_list.append(act_point)
            act_point = p.Point(act_point.x_coord, act_point.y_coord - 1)
            # p_list.append(act_point)
    elif step.direction == DOWN:
        for i in range(step.length):
            p_list.append(act_point)
            act_point = p.Point(act_point.x_coord, act_point.y_coord + 1)
            # p_list.append(act_point)

    return act_point, p_list
