import matplotlib.pyplot as plt


def split_list_of_points(point_list):
    x = []
    y = []

    for p in point_list:
        x.append(p.x_coord)
        y.append(p.y_coord)

    return x, y


def draw_plots(point_path_list, dimensions):
    y_list = []
    x_list = []
    color_list = ['green', 'blue', 'red', 'yellow', 'black', 'magenta', 'cyan', '#4e0000', '#4e00fa']

    for i, point_path in enumerate(point_path_list):
        x, y = split_list_of_points(point_path)
        y_list.append(y)
        x_list.append(x)

        # TODO fix this line
        plt.scatter(x, y, c=color_list[i])   # this line may cause an error

    y_max, x_max = dimensions

    y_min = get_min_elem_from_list_of_lists(y_list)
    x_min = get_min_elem_from_list_of_lists(x_list)

    if y_min > 0:
        y_min = 0
    if x_min > 0:
        x_min = 0

    plt.yticks(range(y_min, y_max, 1))
    plt.xticks(range(x_min, x_max, 1))

    plt.grid(True)
    plt.show()


def get_max_elem_from_list_of_lists(list_of_lists):
    max_elements = map(lambda li: max(li), list_of_lists)
    max_element = max(max_elements)
    return max_element


def get_min_elem_from_list_of_lists(list_of_lists):
    min_elements = map(lambda li: max(li), list_of_lists)
    min_element = max(min_elements)
    return min_element


def visualize_generation_progress(avg_fitting, best_fitness, worst_fitness, generation_amount):
    plt.plot(range(generation_amount), avg_fitting, label='avg')
    plt.plot(range(generation_amount), best_fitness, label='best')
    plt.plot(range(generation_amount), worst_fitness, label='worst')
    plt.legend(loc='upper left')
    plt.show()

