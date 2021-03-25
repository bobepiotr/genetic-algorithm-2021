import ga.solution_.solution as s


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


def parse_population_to_fitting_list(population):
    fitting_list = []

    for solution in population:
        fitting_list.append(solution.fitting)

    return fitting_list
