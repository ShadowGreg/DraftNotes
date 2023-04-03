from controllers.CSVConroller.CSVRecord import Record
from controllers.CSVConroller.CSVReader import Reader
from core.Note import Note
from controllers.CSVConroller.NoteMask import NoteMask

list = []

for i in range(10):
    temp_note = Note(f"gsdfgs{i}", 'sdgfsdfg')
    list.append(temp_note)

# for item in list:
#     print(item.short_text)

mask = NoteMask(Note)
write = Record(mask, '1.csv', ';')
write.write_file_from(list)

reader = Reader(mask, '1.csv', ';')
var = reader.read_data()

for item in var:
    print(item.short_text)
