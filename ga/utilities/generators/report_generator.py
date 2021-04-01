import sys
import ga.structures.pcb_board as bo
import ga.optimizers.genetic_algorithm as ga
import ga.utilities.visualisation as v
import csv
import statistics
from ga.const import *


ITERATIONS = 10


def get_statistic_values(param_list, **kwargs):
    board = bo.PcbBoard()
    board.init_data(kwargs[KW_FILENAME])
    gen_alg = ga.GeneticAlgorithm(board)
    examined_param = kwargs[KW_EXAM_PARAM]
    research_data = {KW_FILENAME: kwargs[KW_FILENAME], KW_EXAM_PARAM: examined_param,
                     KW_GEN_SIZE: [], KW_GEN_AMOUNT: [], KW_TOUR_SIZE: [],
                     KW_BEST_SOL: [], KW_WORST_SOL: [], KW_FITTING_LIST: []}

    for i, param in enumerate(param_list):
        fitting_list = []

        kwargs[examined_param] = param
        best_fitting, worst_fitting, gen_fitting_list \
            = get_population_statistics(gen_alg, **kwargs)

        research_data[KW_GEN_SIZE].append(kwargs[KW_GEN_SIZE])
        research_data[KW_GEN_AMOUNT].append(kwargs[KW_GEN_AMOUNT])
        research_data[KW_TOUR_SIZE].append(kwargs[KW_TOUR_SIZE])
        research_data[KW_BEST_SOL].append(best_fitting)
        research_data[KW_WORST_SOL].append(worst_fitting)
        research_data[KW_FITTING_LIST] += gen_fitting_list

    return research_data


def get_population_statistics(gen_alg, **kwargs):
    pop_fitting_list = []

    best_fitting = sys.maxsize
    worst_fitting = -sys.maxsize

    for j in range(ITERATIONS):
        b_sol, w_sol, res_list, pops = \
            gen_alg.genetic_alg_tournament(kwargs[KW_GEN_SIZE], kwargs[KW_GEN_AMOUNT], kwargs[KW_TOUR_SIZE])

        save_population_progress_plot(j, res_list, **kwargs)

        pop_fitting_list += [item for sub in pops for item in sub]

        if b_sol.fitting < best_fitting:
            best_fitting = b_sol.fitting
        if w_sol.fitting > worst_fitting:
            worst_fitting = w_sol.fitting

    return best_fitting, worst_fitting, pop_fitting_list


def save_research_to_csv_file(research_data, examined_parameter):
    if not os.path.exists(RESEARCH_DATA):
        os.mkdir(RESEARCH_DATA)

    with open(f'{RESEARCH_DATA}/{examined_parameter}_inf.csv', mode='a') as data_file:
        fw = csv.writer(data_file, delimiter=',')
        fw.writerow(["zad", "pop_size", "pop_amount", "tour_size", "best", "worst", "avg", "std"])

        for i in range(len(research_data[KW_GEN_SIZE])):
            fw.writerow([
                research_data[KW_FILENAME][65:69],
                str(research_data[KW_GEN_SIZE][i]),
                str(research_data[KW_GEN_AMOUNT][i]),
                str(research_data[KW_TOUR_SIZE][i]),
                str(research_data[KW_BEST_SOL][i]),
                str(research_data[KW_WORST_SOL][i]),
                str(statistics.mean(research_data[KW_FITTING_LIST][i])),
                str(statistics.stdev(research_data[KW_FITTING_LIST][i]))
            ])


def save_population_progress_plot(iteration, res_list, **kwargs):
    exam_param = kwargs[KW_EXAM_PARAM]
    exam_param_value = kwargs[exam_param]
    img_name = f'{exam_param}_{exam_param_value}_iter{iteration}_{kwargs[KW_FILENAME][65:69]}.png'
    output_dir = os.path.join(RESEARCH_IMAGES, f'{exam_param}_{exam_param_value}')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    v.save_generation_progress_visualisation(*res_list, kwargs[KW_GEN_AMOUNT], f'{output_dir}/{img_name}')


def examine_parameter_influence(filename, exam_param, exam_param_values):
    kwargs = {KW_EXAM_PARAM: exam_param,
              KW_GEN_AMOUNT: DEFAULT_GENERATION_AMOUNT,
              KW_TOUR_SIZE: DEFAULT_TOURNAMENT_SIZE,
              KW_GEN_SIZE: DEFAULT_GENERATION_SIZE,
              KW_FILENAME: filename}

    research_data = get_statistic_values(exam_param_values, **kwargs)
    save_research_to_csv_file(research_data, exam_param)


if __name__ == '__main__':
    examine_parameter_influence(ZAD_2, KW_GEN_SIZE, [50, 100, 200, 300, 400])
    examine_parameter_influence(ZAD_2, KW_GEN_AMOUNT, [100, 200, 300, 400, 500])
    examine_parameter_influence(ZAD_2, KW_TOUR_SIZE, [4, 5, 10, 15, 20, 30])
