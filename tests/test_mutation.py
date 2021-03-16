import unittest

import ga.point as pt
import ga.step as st
import ga.path as pa
from ga.const import *
import ga.solution as s
import ga.visualisation as v
import ga.operators as op
import copy


class TestMutation(unittest.TestCase):
    def setUp(self):
        self.solution = s.Solution()
        self.solution.path_list.append([])

    def test_mutation_1(self):
        path = pa.Path(pt.Point(9, 7), pt.Point(3, 1))
        path.step_list = [st.Step(5, LEFT), st.Step(4, UP), st.Step(3, LEFT), st.Step(1, DOWN)]
        self.solution.path_list[0] = path
        step_list_before_mutation = copy.deepcopy(path.step_list)
        op.mutation(self.solution, 1)
        visualize_solution(step_list_before_mutation, self.solution.path_list[0])

    def test_mutation_2(self):
        path = pa.Path(pt.Point(9, 7), pt.Point(3, 1))
        path.step_list = [st.Step(5, LEFT)]
        self.solution.path_list[0] = path
        step_list_before_mutation = copy.deepcopy(path.step_list)
        op.mutation(self.solution, 1)
        visualize_solution(step_list_before_mutation, self.solution.path_list[0])

    def test_mutation_3(self):
        path = pa.Path(pt.Point(9, 7), pt.Point(3, 1))
        path.step_list = [st.Step(5, LEFT), st.Step(4, UP)]
        self.solution.path_list[0] = path
        step_list_before_mutation = copy.deepcopy(path.step_list)
        op.mutation(self.solution, 1)

        visualize_solution(step_list_before_mutation, self.solution.path_list[0])

    def test_mutation_4(self):
        path = pa.Path(pt.Point(9, 7))
        path.step_list = [st.Step(5, LEFT), st.Step(4, UP), st.Step(1, LEFT)]
        self.solution.path_list[0] = path
        step_list_before_mutation = copy.deepcopy(path.step_list)
        op.mutation(self.solution, 1)
        visualize_solution(step_list_before_mutation, self.solution.path_list[0])

    def test_mutation_5(self):
        path = pa.Path(pt.Point(9, 7))
        path.step_list = [st.Step(2, LEFT), st.Step(2, UP), st.Step(1, LEFT), st.Step(1, UP), st.Step(1, RIGHT),
                          st.Step(3, UP)]
        self.solution.path_list[0] = path
        step_list_before_mutation = copy.deepcopy(path.step_list)
        op.mutation(self.solution, 1)
        visualize_solution(step_list_before_mutation, self.solution.path_list[0])

    def test_mutation_6(self):
        path = pa.Path(pt.Point(9, 7))
        path.step_list = [st.Step(2, LEFT), st.Step(2, UP), st.Step(1, LEFT), st.Step(1, UP), st.Step(1, RIGHT),
                          st.Step(3, UP)]
        self.solution.path_list[0] = path
        step_list_before_mutation = copy.deepcopy(path.step_list)
        op.mutation(self.solution, 1)
        visualize_solution(step_list_before_mutation, self.solution.path_list[0])


def visualize_solution(step_list_before_mutation, pth1):
    pth0 = pa.Path(pt.Point(9, 7), pt.Point(0, 0))
    pth0.step_list = step_list_before_mutation
    visualisation_sol = s.Solution()
    visualisation_sol.path_list = [pth0, pth1]
    print("Before mutation: ", str(pth0))
    print("After mutation: " + str(pth1))
    v.draw_plots(visualisation_sol.parse_to_list_of_points(), (10, 10))


if __name__ == '__main__':
    unittest.main()
