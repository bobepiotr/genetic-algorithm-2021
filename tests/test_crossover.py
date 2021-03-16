import unittest

import ga.solution as s
import ga.pcb_board as b
import ga.operators as op
from ga.const import *


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
        print(f"Potomek jest w {parent1_paths/ total_paths * 100}% rodzicem 1 oraz w "
              f"{parent2_paths/ total_paths * 100}% rodzicem 2.")
        self.assertEqual(is_error, False)


if __name__ == '__main__':
    unittest.main()
