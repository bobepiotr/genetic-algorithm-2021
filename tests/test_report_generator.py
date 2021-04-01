import unittest
import ga.utilities.generators.report_generator as rg
from ga.const import *

# Before running the tests, I recommend to reduce the values of GA parameters in ga/const.py file and the value of
# constant parameter ITERATIONS in ga/utilities/generators/report_generator.py file.


class TestStep(unittest.TestCase):
    def setUp(self):
        self.kwargs = {KW_EXAM_PARAM: '',
                       KW_GEN_AMOUNT: DEFAULT_GENERATION_AMOUNT,
                       KW_TOUR_SIZE: DEFAULT_TOURNAMENT_SIZE,
                       KW_GEN_SIZE: DEFAULT_GENERATION_SIZE,
                       KW_FILENAME: ''}

    def list_equals(self, research_data, param_list, exam_param_name):
        # check if lengths of output lists are correct
        self.assertEqual(len(research_data[KW_BEST_SOL]), len(param_list))
        self.assertEqual(len(research_data[KW_WORST_SOL]), len(param_list))
        self.assertEqual(len(research_data[KW_FITTING_LIST]),
                         calc_fitting_list_len(research_data[KW_GEN_AMOUNT], research_data[KW_GEN_SIZE]))

        # check if lists of default parameters are correct
        if exam_param_name != KW_GEN_SIZE:
            self.assertEqual(research_data[KW_GEN_SIZE], [DEFAULT_GENERATION_SIZE] * len(param_list))
        if exam_param_name != KW_TOUR_SIZE:
            self.assertEqual(research_data[KW_TOUR_SIZE], [DEFAULT_TOURNAMENT_SIZE] * len(param_list))
        if exam_param_name != KW_GEN_AMOUNT:
            self.assertEqual(research_data[KW_GEN_AMOUNT], [DEFAULT_GENERATION_AMOUNT] * len(param_list))

        # check if the examined parameter list is correct
        self.assertEqual(research_data[exam_param_name], param_list)

    def param_test(self, param_list, exam_param_name, filename):
        self.kwargs[KW_EXAM_PARAM] = exam_param_name
        self.kwargs[KW_FILENAME] = filename

        research_data = rg.get_statistic_values(param_list, **self.kwargs)

        self.list_equals(research_data, param_list, exam_param_name)

        print(f'-------{self.kwargs[KW_EXAM_PARAM]}-{self.kwargs[KW_FILENAME][65:69]}-------')
        print_research_data(research_data)
        print(f'----------------------------------------------------------------------------------')

    def test_get_stat_val_gen_amount_zad2(self):
        param_list = [1, 2, 3, 4]
        self.param_test(param_list, KW_GEN_AMOUNT, ZAD_2)

    def test_get_stat_val_gen_size_zad2(self):
        param_list = [11, 15, 20, 25]
        self.param_test(param_list, KW_GEN_SIZE, ZAD_2)

    def test_get_stat_val_tour_size_zad2(self):
        param_list = [1, 5, 6, 8]
        self.param_test(param_list, KW_TOUR_SIZE, ZAD_2)


def print_research_data(research_data):
    for kw, elem in research_data.items():
        print(f'{kw}: {elem}')


def calc_fitting_list_len(gen_amount, gen_size):
    fitting_list_len = 0
    for gen_am, gen_siz in zip(gen_amount, gen_size):
        fitting_list_len += rg.ITERATIONS * gen_am * gen_siz
    return fitting_list_len


if __name__ == '__main__':
    unittest.main()