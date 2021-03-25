import ga.utilities.data_loading as dl


class PcbBoard:
    def __init__(self):
        self.point_list = []
        self.dimensions = (0, 0)

    def init_data(self, file_name):
        self.dimensions, self.point_list = dl.get_data_from_text_file(file_name)
