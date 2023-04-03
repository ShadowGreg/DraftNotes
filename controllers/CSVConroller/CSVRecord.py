import io

from controllers.CSVConroller.NoteMask import NoteMask


class Record:
    def __init__(self, anonymous_class: NoteMask, filename, separator: str):
        self.anonymous_class = anonymous_class
        self.filename = filename
        self.s = separator

    def write_file_from(self, collection: [NoteMask]):
        with io.open(self.filename, 'w', encoding='utf-8') as file:
            for item in collection:
                row = f'{item.id}{self.s}{item.title}' \
                      f'{self.s}{item.body}{self.s}{item.created_at}' \
                      f'{self.s}{item.modified_at} \n'
                file.writelines(row)
