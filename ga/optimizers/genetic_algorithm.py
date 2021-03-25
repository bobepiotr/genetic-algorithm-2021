import ga.utilities.generators.population_generator as pg
import ga._operators.selection_operators as so
import ga._operators.operators as o
import random as ran
import copy as c
import sys
from ga.const import *
import ga.solution as s


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

    def genetic_alg_tournament(self, generation_size, generation_amount, tournament_size):
        population = self.population_generator.generate_population(generation_size)
        best_solution = pick_best_solution(population)
        worst_solution = pick_worst_solution(population)

        # necessary for research
        fitting_list = population_to_fitting_list(population)  # list of fittings of each population member
        populations = [fitting_list]
        avg_fitting = [sum(fitting_list) / generation_size]
        best_fitting = [min(fitting_list)]
        worst_fitting = [max(fitting_list)]

        for i in range(generation_amount - 1):
            new_population = []
            while len(new_population) < generation_size:
                parent_1 = so.tournament_selection(population, tournament_size)
                parent_2 = so.tournament_selection(population, tournament_size)
                if ran.random() < self.crossover_probability:
                    child = o.crossover(parent_1, parent_2)
                else:
                    child = c.deepcopy(parent_1)
                if ran.random() < self.mutation_probability:
                    o.mutation(child, mutation_power=ran.randint(1, 3), kind='split')

                child.calculate_and_set_fitting(self.board)
                new_population.append(child)
                if child.fitting < best_solution.fitting:
                    best_solution = c.deepcopy(child)
                if child.fitting > worst_solution.fitting:
                    worst_solution = c.deepcopy(child)

            population = c.deepcopy(new_population)
            fitting_list = population_to_fitting_list(population)    # list of fittings of each population member
            populations.append(fitting_list)
            best_fitting.append(min(fitting_list))        # best fitting value in current population
            worst_fitting.append(max(fitting_list))       # worst_fitting value in current population
            avg_fitting.append(sum(fitting_list) / generation_size)      # average fitting in current population

        # best solution, worst solution, research necessities, fitting of all generated individuals
        return best_solution, worst_solution, (avg_fitting, best_fitting, worst_fitting), populations


def pick_best_solution(population):
    best_solution = s.Solution()
    best_solution.fitting = sys.maxsize

    for sol in population:
        if sol.fitting < best_solution.fitting:
            best_solution = sol

    return best_solution


def pick_worst_solution(population):
    worst_solution = s.Solution()
    worst_solution.fitting = -sys.maxsize

    for sol in population:
        if sol.fitting > worst_solution.fitting:
            worst_solution = sol

    return worst_solution


def population_to_fitting_list(population):
    fitting_list = []
    for s in population:
        fitting_list.append(s.fitting)

    return fitting_list


def population_log(population, pop_number):
    print('--------------'+str(pop_number)+'--------------------')
    for s in population:
        print('-----------connection-----------------')
        for p in s.path_list:
            print(p)
        print('--------------------------------------')
