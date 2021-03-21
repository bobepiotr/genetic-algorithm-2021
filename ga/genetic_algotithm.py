import ga.population_generator as pg
import ga.selection_operators as so
import ga.operators as o
import random as ran
import copy as c
import sys
from ga.const import *
import matplotlib


class GeneticAlgorithm:
    def __init__(self, brd):
        self.board = brd
        self.population_generator = pg.PopulationGenerator(self.board)
        self.crossover_probability = CROSSOVER_PROBABILITY
        self.mutation_probability = MUTATION_PROBABILITY

    def set_mutation_probability(self, new_value):
        self.mutation_probability = new_value

    def set_crossover_probability(self, new_value):
        self.crossover_probability = new_value

    def genetic_alg(self, generation_size, generation_amount):
        population = self.population_generator.generate_population(generation_size)
        best_solution = pick_best_solution(population)

        new_population = []
        is_mutation = False
        is_copy = False

        for i in range(generation_amount):
            while len(new_population) < generation_size:
                parent_1 = so.tournament_selection(population, 10)
                parent_2 = so.tournament_selection(population, 10)

                if ran.random() < self.crossover_probability:
                    child = o.crossover(parent_1, parent_2)
                else:
                    child = c.deepcopy(parent_1)
                    is_copy = True

                if ran.random() < self.mutation_probability:
                    o.mutation(child)
                    is_mutation = True

                if is_mutation or not is_copy:
                    child.calculate_and_set_fitting(self.board)
                    is_mutation = False
                    is_copy = False

                new_population.append(child)
                if child.fitting < best_solution.fitting:
                    best_solution = child
            population = c.deepcopy(new_population)
            new_population = []

        return best_solution

    def genetic_alg_2(self, generation_size, generation_amount):
        population = self.population_generator.generate_population(generation_size)
        best_solution = pick_best_solution(population)

        new_population = []
        is_mutation = False
        is_copy = False

        for i in range(generation_amount - 1):
            while len(new_population) < generation_size:
                parent_1 = so.tournament_selection(population, 10)
                parent_2 = so.tournament_selection(population, 10)

                if ran.random() < self.crossover_probability:
                    child = o.crossover(parent_1, parent_2)
                else:
                    child = c.deepcopy(parent_1)
                    is_copy = True

                if ran.random() < self.mutation_probability:
                    o.mutation(child)
                    is_mutation = True

                if is_mutation or is_copy:
                    child.calculate_and_set_fitting(self.board)
                    is_mutation = False
                    is_copy = False

                new_population.append(child)
                if child.fitting < best_solution.fitting:
                    best_solution = child
            population = c.deepcopy(new_population)
            rest_population = self.population_generator.generate_population(int(generation_size / 2))
            population += rest_population
            new_population = []
        return best_solution


def pick_best_solution(population):
    best_fitness = sys.maxsize
    best_solution = None

    for sol in population:
        if sol.fitting < best_fitness:
            best_solution = sol

    return best_solution


def get_avg_fitting(population):
    fitting_sum = 0
    for s in population:
        fitting_sum += s.fitting

    return fitting_sum / len(population)

