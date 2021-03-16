import ga.path_creator as sc
import ga.punishment as pn
import ga.path as pa

from ga.const import *


class Solution:
    def __init__(self):
        self.path_list = []    # [[step1, step2, step3, ...], [step1, step2, step3, ...]]
        self.fitting = 0

    def __lt__(self, other):
        if isinstance(other, Solution):
            return self.fitting < other.fitting
        return False

    def __gt__(self, other):
        if isinstance(other, Solution):
            return self.fitting > other.fitting
        return False

    def __radd__(self, other):
        return other + self.fitting

    def create_solution(self, board):
        for p1, p2 in board.point_list:
            path = pa.Path(p1, p2)
            path.create_random_path(board.dimensions)
            self.path_list.append(path)

    def parse_to_list_of_points(self):
        path_point_list = []    # [[p1, p2, p3, ...], [p1, p2, p3, ...], ...]
        for path in self.path_list:
            p_list = path.convert_point_list()
            path_point_list.append(p_list)

        return path_point_list

    def present_solution(self, brd):
        list_of_points = self.parse_to_list_of_points()

        for point_list, path in zip(list_of_points, self.path_list):
            print(f"Path between point {point_list[0]} and {point_list[-1]}:")
            for point in point_list:
                print(str(point), end=' ')
            print('')
            print(path)

        print(self.calculate_fitting_elements(brd))

    def calculate_fitting_elements(self, board):
        point_list = self.parse_to_list_of_points()

        intersections = pn.get_intersections_amount(point_list)
        total_path_length = pn.get_total_path_length(self.path_list)
        steps_amount = pn.get_steps_amount(self.path_list)
        out_paths, out_paths_amount = pn.get_out_paths_amount(point_list, board.dimensions)
        total_out_segments_length = pn.get_total_length_of_out_segments(out_paths, board.dimensions)

        return intersections, total_path_length, steps_amount, out_paths_amount, total_out_segments_length

    def calculate_and_set_fitting(self, board):
        inter, total_path_len, steps_am, out_pth_len, total_out_seg_len = self.calculate_fitting_elements(board)

        self.fitting = INTERSECTION_WEIGHT * inter \
            + LENGTH_WEIGHT * total_path_len\
            + STEPS_WEIGHT * steps_am\
            + OUT_PATHS_WEIGHT * out_pth_len\
            + OUT_PATHS_LENGTH_WEIGHT * total_out_seg_len
