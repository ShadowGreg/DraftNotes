import io

from controllers.CSVConroller.NoteMask import NoteMask


class Reader:
    def __init__(self, anonymous_class: NoteMask, file_path, separator: str):
        self.anonymous_class = anonymous_class
        self.file_path = file_path
        self.s = separator

    def read_data(self):
        instances = []
        with io.open(self.file_path, 'r', encoding='utf-8') as file:
            temp = file.read().split('\n')
            for row in temp:
                if row != '':
                    array = row.split(';')
                    instances.append(self.anonymous_class.make_base_note(array))

        return instances
