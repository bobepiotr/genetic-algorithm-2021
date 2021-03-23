import random as ran
import ga.population_generator as pg
import math
import numpy as np


def tournament_selection(population, tournament_size):
    population_size = len(population)
    if tournament_size > population_size:
        return []

    tournament_set = set()

    while len(tournament_set) < tournament_size:
        random_index = ran.randint(0, population_size - 1)
        tournament_set.add(population[random_index])

    best_solution = tournament_set.pop()

    for solution in tournament_set:
        if solution.fitting < best_solution.fitting:
            best_solution = solution

    return best_solution


# def roulette_selection(population):
#     probabilities_inverted = []
#     probabilities = []
#     max_fitting = sum_population_fittings(population)
#
#     for solution in population:
#         prob = (1 - solution.fitting / max_fitting) * max_fitting
#         probabilities_inverted.append(prob)
#
#     max_fitting = sum(probabilities_inverted)
#
#     for inv_prob, sol in zip(probabilities_inverted, population):
#         prob = inv_prob / max_fitting
#         probabilities.append(prob)
#
#     best = np.random.choice(population, p=probabilities)
#
#     return best


def roulette_selection(population):
    fitting_list = pg.parse_population_to_fitting_list(population)
    min_fitting = min(fitting_list)

    weight = []

    for fitting in fitting_list:
        weight.append(min_fitting/fitting)

    winner = ran.choices(population, weight)[0]

    return winner


def sum_population_fittings(population):
    fitting_sum = 0
    for sol in population:
        fitting_sum += sol.fitting

    return fitting_sum
