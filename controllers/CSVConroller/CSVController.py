from controllers.CSVConroller.CSVReader import Reader
from controllers.CSVConroller.CSVRecord import Record
from controllers.CSVConroller.NoteMask import NoteMask
from core.Note import Note


class CSVController:
    def __init__(self, file_name: str):
        self.mask = NoteMask(Note)
        self.file_name = file_name

    def write(self, data: [], separator: str = ';'):
        Record(self.mask, self.file_name, separator).write_file_from(data)

    def read(self, separator: str = ';'):
        return Reader(self.mask, self.file_name, separator).read_data()
