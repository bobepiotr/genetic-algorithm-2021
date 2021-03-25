import ga.structures.point as point


def get_data_from_text_file(file_path):
    list_of_points = []     # [(Point1, Point2), (Point1, Point2), ...]

    with open(file_path) as f:
        lines = f.read().split("\n")
        dim = lines[0].split(";")
        dimensions = (int(dim[0]), int(dim[1]))
        lines.pop(0)
        lines.pop(-1)

        for l in lines:
            x1, y1, x2, y2 = l.split(";")
            p1 = point.Point(int(x1), int(y1))
            p2 = point.Point(int(x2), int(y2))
            list_of_points.append((p1, p2))

    return dimensions, list_of_points


def print_list_of_points(lis):
    for p1, p2 in lis:
        print(f'{p1}, {p2}')


def test_data_loading():
    dims, lis = get_data_from_text_file("exercises/zad0.txt")
    print_list_of_points(lis)
    print(dims)


if __name__ == '__main__':
    test_data_loading()
