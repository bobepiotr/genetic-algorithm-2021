
def get_intersections_amount(paths_point_list):
    dct = {}
    for path in paths_point_list:
        for p in path:
            point_tuple = (p.x_coord, p.y_coord)
            if point_tuple in dct.keys():
                dct[point_tuple] += 1
            else:
                dct[point_tuple] = 0

    crossings = sum(dct.values())
    return crossings


def get_total_path_length(path_list):
    total_path_length = 0
    for path in path_list:
        for step in path.step_list:
            total_path_length += step.length

    return total_path_length


def get_steps_amount(path_list):
    steps_amount = 0
    prev_direction = -1

    for path in path_list:
        for step in path.step_list:
            if step.direction != prev_direction:
                steps_amount += 1
            prev_direction = step.direction
        prev_direction = -1
    return steps_amount


def get_out_paths_amount(point_list, dimensions):
    out_paths_amount = 0
    out_paths = []

    for path in point_list:
        for point in path:
            if is_point_out(point, dimensions):
                out_paths_amount += 1
                out_paths.append(path)
                break
    return out_paths, out_paths_amount


def get_total_length_of_out_segments(out_paths_list, dimensions):
    total_length_of_out_paths = 0

    for path in out_paths_list:
        act_length_of_out_paths = 0
        for point in path:
            if is_point_out(point, dimensions):
                act_length_of_out_paths += 1
        act_length_of_out_paths += 1
        total_length_of_out_paths += act_length_of_out_paths

    return total_length_of_out_paths


def is_point_out(point, dims):
    x_border, y_border = dims
    return point.x_coord > x_border or point.y_coord > y_border or point.x_coord < 0 or point.y_coord < 0
