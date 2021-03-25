import ga.solution.solution as sol
import random as ran
import ga.structures.step as st
from ga.const import *
import copy as c


def crossover(parent1, parent2):
    child = sol.Solution()
    parent1_path_list = parent1.path_list
    parent2_path_list = parent2.path_list

    for path_1, path_2 in zip(parent1_path_list, parent2_path_list):
        inheritance = c.deepcopy(path_1) if ran.random() > 0.5 else c.deepcopy(path_2)
        child.path_list.append(inheritance)

    return child


def mutation(solution, step_index=-1, mutation_turn=-1, mutation_power=1):
    random_path_index = ran.randint(0, len(solution.path_list) - 1)
    mutation_path = solution.path_list[random_path_index]
    mutation_list = mutation_path.step_list
    step_amount = len(mutation_list)
    random_step_index = step_index if step_index != -1 else ran.randint(0, step_amount - 1)
    mutation_step = mutation_list[random_step_index]

    # horizontal mutations
    if mutation_step.direction == LEFT or mutation_step.direction == RIGHT:
        create_path(mutation_list, random_step_index, step_amount, UP, DOWN, mutation_power, mutation_turn)
    else:  # vertical mutations
        create_path(mutation_list, random_step_index, step_amount, RIGHT, LEFT, mutation_power, mutation_turn)

    mutation_path.remove_zero_steps()
    mutation_path.concat_same_direction_steps()


def setup_neighbours(mutation_list, random_step_index, step_amount, mutation_direction, dir_1, dir_2):
    if random_step_index == 0:                       # no left neighbour
        left_ngb_dir = dir_1 if mutation_direction == dir_1 else dir_2
        mutation_list.insert(0, st.Step(0, left_ngb_dir))
        random_step_index += 1
        step_amount += 1

    if random_step_index == step_amount - 1:         # no right neighbour
        right_ngb_dir = dir_1 if mutation_direction == dir_1 else dir_2
        mutation_list.append(st.Step(0, right_ngb_dir))
        step_amount += 1

    return mutation_list[random_step_index - 1], mutation_list[random_step_index+1]


def create_path(mutation_list, random_step_index, step_amount, dir_1, dir_2, mutation_power, mutation_turn=-1):
    # drawing the direction of the mutation
    mutation_turn = mutation_turn if mutation_turn != -1 else ran.choice([dir_1, dir_2])

    # assigning neighbours
    # left neighbour - element in the step_list before the step that is mutating
    # left neighbour - element in the step_list after the step that is mutating
    left_neighbour, right_neighbour = \
        setup_neighbours(mutation_list, random_step_index, step_amount, mutation_turn, dir_1, dir_2)

    if mutation_turn == dir_1:
        if left_neighbour.direction == right_neighbour.direction:
            if left_neighbour.direction == dir_1:
                left_neighbour.length += mutation_power
                right_neighbour.length -= mutation_power
            else:
                left_neighbour.length -= mutation_power
                right_neighbour.length += mutation_power
        elif left_neighbour.direction == dir_1 and right_neighbour.direction == dir_2:
            left_neighbour.length += mutation_power
            right_neighbour.length += mutation_power
        elif left_neighbour.direction == dir_2 and right_neighbour.direction == dir_1:
            left_neighbour.length -= mutation_power
            right_neighbour.length -= mutation_power
    else:
        if left_neighbour.direction == right_neighbour.direction:
            if left_neighbour.direction == dir_1:
                left_neighbour.length -= mutation_power
                right_neighbour.length += mutation_power
            else:
                left_neighbour.length += mutation_power
                right_neighbour.length -= mutation_power
        elif left_neighbour.direction == dir_1 and right_neighbour.direction == dir_2:
            left_neighbour.length -= mutation_power
            right_neighbour.length -= mutation_power
        elif left_neighbour.direction == dir_2 and right_neighbour.direction == dir_1:
            left_neighbour.length += mutation_power
            right_neighbour.length += mutation_power

    fix_negative_values(mutation_list)


def fix_negative_values(step_list):
    for step in step_list:
        if step.length < 0:
            step.set_oppose_direction()
