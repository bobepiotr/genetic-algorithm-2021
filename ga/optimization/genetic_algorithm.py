import ga.generators.population_generator as pg
import ga.operators.selection_operators as so
import ga.operators.operators as o
import random as ran
import copy as c
import sys
from ga.const import *
import ga.solution.solution as s


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

        # necessary for research
        avg_fitting = []
        best_fitting = []
        best_fitting_2 = []
        worst_fitting = []

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
                    o.mutation(child, mutation_power=ran.randint(1, 4))
                    is_mutation = True
                if is_mutation or not is_copy:
                    child.calculate_and_set_fitting(self.board)
                    is_mutation = False
                    is_copy = False
                new_population.append(child)
                if child.fitting < best_solution.fitting:
                    best_solution = child

            fitting_list = population_to_fitting_list(population)    # list of fittings of each population member
            best_fitting.append(min(fitting_list))        # best fitting value in current population
            best_fitting_2.append(pick_best_solution(population).fitting)
            worst_fitting.append(max(fitting_list))       # worst_fitting value in current population
            avg_fitting.append(sum(fitting_list) / generation_size)      # average fitting in current population
            population = c.deepcopy(new_population)
            new_population = []
        return best_solution, (avg_fitting, best_fitting, worst_fitting)


def pick_best_solution(population):
    best_solution = s.Solution()
    best_solution.fitting = sys.maxsize

    for sol in population:
        if sol.fitting < best_solution.fitting:
            best_solution = sol

    return best_solution


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
