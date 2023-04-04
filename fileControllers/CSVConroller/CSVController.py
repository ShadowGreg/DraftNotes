import os

from fileControllers.CSVConroller.CSVReader import Reader
from fileControllers.CSVConroller.CSVRecord import Record
from fileControllers.CSVConroller.NoteMask import NoteMask
from core.Note import Note
from fileControllers.FileController import FileController


class CSVController(FileController):
    def __init__(self, file_name: str):
        self.mask = NoteMask(Note)
        self.file_name = file_name
        if not os.path.exists(file_name):
            self.create_empty_file()

    def write(self, data: [], separator: str = ';'):
        Record(self.mask, self.file_name, separator).write_file_from(data)

    def read(self, separator: str = ';'):
        return Reader(self.mask, self.file_name, separator).read_data()

    def create_empty_file(self):
        # os.mkdir(str(self.file_name.split('/')[1]))
        open(self.file_name, 'w+')
