from sys import maxsize
import ga.solution_.solution as s
import ga.utilities.generators.population_generator as pg
import time as t


class RandomMethod:
    def __init__(self, brd):
        self.board = brd

    def random_function(self, amount):
        best_solution = s.Solution()
        best_solution.fitting = maxsize

        for i in range(amount):
            solution = s.Solution()
            solution.create_solution(self.board)
            solution.calculate_and_set_fitting(self.board)
            if solution.fitting < best_solution.fitting:
                best_solution = solution

        return best_solution

    def random_function_research(self, amount):
        best_solution = s.Solution()
        best_solution.fitting = maxsize
        worst_solution = s.Solution()
        worst_solution.fitting = -maxsize
        # research
        pop_gen = pg.PopulationGenerator(self.board)
        population = pop_gen.generate_population(amount)
        fitting_list = pg.parse_population_to_fitting_list(population)
        # necessary for research
        # best sol, worst sol, fitting list
        return min(fitting_list), max(fitting_list), fitting_list

    def random_function_time(self, duration):
        best_solution = s.Solution()
        best_solution.fitting = maxsize

        start = t.time()
        stop = t.time()

        while duration > (stop - start):
            solution = s.Solution()
            solution.create_solution(self.board)
            solution.calculate_and_set_fitting(self.board)
            if solution.fitting < best_solution.fitting:
                best_solution = solution
            stop = t.time()

        return best_solution
