import random as ran
import ga.point as p
import ga.step as st
from ga.const import *
import math as m


def create_random_path(start, stop, dimensions):
    step_list = []    # [Step(length, direction), Step(length, direction), Step(length, direction) ...]
    x, y = dimensions
    maximum_step_length = int((x + y) / m.sqrt(x + y))
    maximum_steps_amount = int((x + y) / 2)
    steps_amount = ran.randint(1, maximum_steps_amount)
    actual_position = start
    previous_direction = -1

    for i in range(steps_amount):
        direction = ran.choice([RIGHT, LEFT, UP, DOWN])
        while is_step_back(previous_direction, direction):
            direction = ran.choice([RIGHT, LEFT, UP, DOWN])
        length = ran.randint(1, maximum_step_length)

        length, actual_position = go_n_moves_in_direction(direction, length, actual_position, stop)
        step_list.append(st.Step(length, direction))
        previous_direction = direction

        if actual_position == stop:
            return step_list

    step_list += find_target(actual_position, stop)

    return step_list


def go_n_moves_in_direction(direction, length, actual_position, stop):
    x_coord = actual_position.x_coord
    y_coord = actual_position.y_coord

    stop_xy_coord = (stop.x_coord, stop.y_coord)

    for i in range(length):
        if (x_coord, y_coord) != stop_xy_coord:
            if direction == RIGHT:
                x_coord += 1
            elif direction == LEFT:
                x_coord -= 1
            elif direction == UP:
                y_coord -= 1
            elif direction == DOWN:
                y_coord += 1
        else:
            return i, p.Point(x_coord, y_coord)
    return length, p.Point(x_coord, y_coord)


def find_target(act_position, stop):
    x_coord = act_position.x_coord
    y_coord = act_position.y_coord
    stop_x_coord = stop.x_coord
    stop_y_coord = stop.y_coord

    horizontal_length = 0
    horizontal_direction = 0
    vertical_length = 0
    vertical_direction = 0

    if y_coord != stop_y_coord:
        vertical_length = abs(stop_y_coord - y_coord)
        if y_coord < stop_y_coord:
            vertical_direction = DOWN
        else:
            vertical_direction = UP

    if x_coord != stop_x_coord:
        horizontal_length = abs(stop_x_coord - x_coord)
        if x_coord < stop_x_coord:
            horizontal_direction = RIGHT
        else:
            horizontal_direction = LEFT

    if horizontal_length != 0 and vertical_length != 0:
        return [st.Step(vertical_length, vertical_direction), st.Step(horizontal_length, horizontal_direction)]
    elif horizontal_length != 0:
        return [st.Step(horizontal_length, horizontal_direction)]
    elif vertical_length != 0:
        return [st.Step(vertical_length, vertical_direction)]
    else:
        return []


def is_step_back(prev_direction, act_direction):
    if prev_direction == RIGHT:
        return act_direction == LEFT
    elif prev_direction == LEFT:
        return act_direction == RIGHT
    elif prev_direction == UP:
        return act_direction == DOWN
    elif prev_direction == DOWN:
        return act_direction == UP
    else:
        return False
