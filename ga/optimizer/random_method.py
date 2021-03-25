from sys import maxsize
import ga.solution.solution as s
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
