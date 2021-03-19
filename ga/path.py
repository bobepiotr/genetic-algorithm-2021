from ga.point import *
import ga.path_creator as pc
import ga.step as st
import copy as c


class Path:
    def __init__(self, sta=Point(0, 0), sto=Point(0, 0)):
        self.step_list = []
        self.start = sta
        self.stop = sto

    def __str__(self):
        return step_list_to_string(self.step_list)

    def __eq__(self, other):
        if isinstance(other, Path):
            return self.step_list == other.step_list
        else:
            return False

    def add_step(self, step):
        self.step_list.append(step)

    def create_random_path(self, dimensions):
        self.step_list = pc.create_random_path(self.start, self.stop, dimensions)
        self.concat_same_direction_steps()

    def convert_point_list(self):
        p_list = []
        act_point = Point(self.start.x_coord, self.start.y_coord)

        for s in self.step_list:
            act_point, step_point_list = s.convert_to_point_list(act_point)
            p_list += step_point_list
        p_list.append(act_point)

        return p_list

    def concat_same_direction_steps(self):
        prev_step = st.Step(0, -1)
        new_step_list = []

        for step in self.step_list:
            if prev_step.direction == step.direction:
                prev_step.length += step.length
            else:
                new_step_list.append(step)
                prev_step = step

        self.step_list = new_step_list

    def remove_zero_steps(self):
        new_step_list = []

        for step in self.step_list:
            if step.length != 0:
                new_step_list.append(step)

        self.step_list = new_step_list


def step_list_to_string(step_list):
    size = len(step_list)
    step_list_str = ''
    for i, step in enumerate(step_list):
        step_list_str += str(step)
        if i < size - 1:
            step_list_str += ' -> '
    return step_list_str
