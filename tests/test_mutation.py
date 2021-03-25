import unittest

import ga.structures.point as pt
import ga.structures.step as st
import ga.structures.path as pa
from ga.const import *
import ga.solution.solution as s
import ga.utilities.visualisation as v
import ga.operators.operators as op
import copy


class TestMutation(unittest.TestCase):
    def setUp(self):
        self.solution = s.Solution()
        self.path = pa.Path(pt.Point(9, 7))
        self.path_before_mut = pa.Path(pt.Point(9, 7))

    def mutate(self, step_list, step_index, mutation_turn):
        self.path.step_list = step_list
        self.solution.path_list = [self.path]
        step_list_before_mut = copy.deepcopy(step_list)
        self.path_before_mut.step_list = step_list_before_mut

        op.mutation(self.solution, step_index, mutation_turn)
        print("Before mutation: ", str(self.path_before_mut))
        print("After mutation: " + str(self.path))

        self.solution.path_list = [self.path_before_mut, self.path]
        v.draw_plots(self.solution.parse_to_list_of_points(), (10, 10))

    def test_mutation_1(self):
        step_list = [st.Step(5, LEFT), st.Step(4, UP), st.Step(3, LEFT), st.Step(1, DOWN)]
        self.mutate(step_list, 2, UP)

    def test_mutation_2(self):
        step_list = [st.Step(5, LEFT)]
        self.mutate(step_list, 0, DOWN)

    def test_mutation_3(self):
        step_list = [st.Step(5, LEFT), st.Step(4, UP)]
        self.mutate(step_list, 1, RIGHT)

    def test_mutation_4(self):
        step_list = [st.Step(5, LEFT), st.Step(4, UP), st.Step(1, LEFT)]
        self.mutate(step_list, 1, LEFT)

    def test_mutation_5(self):
        step_list = [st.Step(2, LEFT), st.Step(2, UP), st.Step(1, LEFT), st.Step(1, UP), st.Step(1, RIGHT),
                     st.Step(3, UP)]
        self.mutate(step_list, 3, RIGHT)

    def test_mutation_6(self):
        step_list = [st.Step(2, LEFT), st.Step(2, UP), st.Step(1, LEFT), st.Step(1, UP), st.Step(1, RIGHT),
                     st.Step(3, UP)]
        self.mutate(step_list, 5, LEFT)


if __name__ == '__main__':
    unittest.main()
