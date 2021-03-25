import ga.solution as s


class PopulationGenerator:
    def __init__(self, brd):
        self.board = brd

    def generate_population(self, amount):
        population = []

        for i in range(amount):
            solution = s.Solution()
            solution.create_solution(self.board)
            solution.calculate_and_set_fitting(self.board)
            population.append(solution)

        return population
