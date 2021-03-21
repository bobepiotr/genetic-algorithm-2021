import unittest

import ga.solution as s
import ga.pcb_board as b
import ga.operators as op
from ga.const import *
import ga.step as st


class TestPath(unittest.TestCase):
    def setUp(self):
        self.board = b.PcbBoard()
        self.board.init_data(ZAD_0)
        self.solution1 = s.Solution()
        self.solution2 = s.Solution()

        self.solution1.create_solution(self.board)
        self.solution2.create_solution(self.board)

    def test_crossover_1(self):
        solution3 = op.crossover(self.solution1, self.solution2)
        is_error = False
        parent1_paths = 0
        parent2_paths = 0
        total_paths = len(solution3.path_list)

        for path in solution3.path_list:
            if path in self.solution1.path_list:
                parent1_paths += 1
            elif path in self.solution2.path_list:
                parent2_paths += 1
            else:
                is_error = True
                break

        if len(solution3.path_list) != len(self.solution1.path_list) or\
                len(solution3.path_list) != len(self.solution2.path_list):
            is_error = True

        if not is_error:
            print(f"Child is in {parent1_paths/ total_paths * 100}% parent 1 and in "
                f"{parent2_paths/ total_paths * 100}% parent 2.")

        self.assertEqual(is_error, False)

    def test_crossover_2(self):
        child = op.crossover(self.solution1, self.solution2)

        child.path_list[0].step_list[0] = st.Step(99999, 1)
        child.path_list[1].step_list[0] = st.Step(99999, 1)

        print_paths(child, 'child')
        print_paths(self.solution1, 'parent 1')
        print_paths(self.solution2, 'parent 2')


def print_paths(solution, name):
    print(f'------------{name}------------')
    for p in solution.path_list:
        print(str(p))
    print("")


if __name__ == '__main__':
    unittest.main()
