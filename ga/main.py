import ga.solution as s
import ga.pcb_board as b
import ga.visualisation as v
from ga.const import *
import ga.random_method as rm
import time
import ga.selection_operators as so
import ga.population_generator as pg


def create_one_solution(file_path):
    brd = b.PcbBoard()
    brd.init_data(file_path)

    solution = s.Solution()
    solution.create_solution(brd)

    solution.present_solution(brd)

    v.draw_plots(solution.parse_to_list_of_points(), brd.dimensions)


def random_function(brd, amount):
    rand_func = rm.RandomMethod(brd)
    start = time.time()
    best_sol = rand_func.random_function(amount)
    stop = time.time()

    print(f"Total time: {stop - start} seconds")

    v.draw_plots(best_sol.parse_to_list_of_points(), brd.dimensions)


def random_function_time(brd, duration):
    rand_func = rm.RandomMethod(brd)
    start = time.time()
    best_sol = rand_func.random_function_time(duration)
    stop = time.time()
    print(f"Total time: {stop - start} seconds")

    v.draw_plots(best_sol.parse_to_list_of_points(), brd.dimensions)


def tournament_selection(brd, tournament_size, amount):
    pop_gen = pg.PopulationGenerator(brd)
    population = pop_gen.generate_population(amount)
    tournament_winner = so.tournament_selection(population, tournament_size)
    tournament_winner.present_solution(brd)
    v.draw_plots(tournament_winner.parse_to_list_of_points(), brd.dimensions)


def roulette_selection(brd, amount):
    pop_gen = pg.PopulationGenerator(brd)
    population = pop_gen.generate_population(amount)

    roulette_winner = so.roulette_selection(population)
    roulette_winner.present_solution(brd)
    v.draw_plots(roulette_winner.parse_to_list_of_points(), brd.dimensions)


if __name__ == '__main__':
    AMOUNT_OF_INDIVIDUALS = 1_000
    TIME = 500
    TOURNAMENT_SIZE = 10

    board = b.PcbBoard()
    board.init_data(ZAD_0)

    # create_one_solution(ZAD_0)
    # random_function(board, AMOUNT_OF_INDIVIDUALS)
    # tournament_selection(board, TOURNAMENT_SIZE, AMOUNT_OF_INDIVIDUALS)
    # roulette_selection(board, AMOUNT_OF_INDIVIDUALS)
