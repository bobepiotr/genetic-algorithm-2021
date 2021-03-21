import unittest

import ga.point as pt
import ga.step as st
import ga.path as pa
from ga.const import *
import ga.solution as s
import ga.visualisation as v
import ga.operators as op
import copy


class TestSplitMutation(unittest.TestCase):
    def setUp(self):
        self.solution = s.Solution()
        self.path = pa.Path(pt.Point(9, 7))
        self.path_before_mut = pa.Path(pt.Point(9, 7))

    def split_mutate(self, step_list, step_index, mutation_turn, kind=''):
        self.path.step_list = step_list
        self.solution.path_list = [self.path]
        step_list_before_mut = copy.deepcopy(step_list)
        self.path_before_mut.step_list = step_list_before_mut

        op.mutation(self.solution, step_index, mutation_turn, kind=kind)
        print("Before mutation: ", str(self.path_before_mut))
        print("After mutation: " + str(self.path))

        self.solution.path_list = [self.path_before_mut, self.path]
        v.draw_plots(self.solution.parse_to_list_of_points(), (10, 10))

    def test_split_mutation_1(self):
        step_list = [st.Step(5, LEFT), st.Step(4, UP), st.Step(5, LEFT), st.Step(1, DOWN)]
        self.split_mutate(step_list, 2, UP, kind='split')

    def test_split_mutation_2(self):
        step_list = [st.Step(5, LEFT)]
        self.split_mutate(step_list, 0, DOWN, kind='split')

    def test_split_mutation_3(self):
        step_list = [st.Step(5, LEFT), st.Step(4, UP)]
        self.split_mutate(step_list, 0, UP, kind='split')

    def test_split_mutation_4(self):
        step_list = [st.Step(5, LEFT), st.Step(4, UP), st.Step(1, LEFT)]
        self.split_mutate(step_list, 1, LEFT, kind='split')

    def test_split_mutation_5(self):
        step_list = [st.Step(2, LEFT), st.Step(2, UP), st.Step(1, LEFT), st.Step(1, UP), st.Step(1, RIGHT),
                     st.Step(3, UP)]
        self.split_mutate(step_list, 3, RIGHT, kind='split')

    def test_split_mutation_6(self):
        step_list = [st.Step(2, LEFT), st.Step(2, UP), st.Step(1, LEFT), st.Step(1, UP), st.Step(1, RIGHT),
                     st.Step(6, UP)]
        self.split_mutate(step_list, 5, LEFT, kind='split')


if __name__ == '__main__':
    unittest.main()