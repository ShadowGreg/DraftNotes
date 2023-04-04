from core.BaseNote import BaseNote


class Filter:
    def __init__(self, abstract_class: BaseNote, array: [BaseNote]):
        self.abstract_class = abstract_class
        self.array = array

    def filter_data(self, date=None):
        if date is None:
            return list(self.array)
        else:
            array = []
            for item in self.array:
                if date in item.created_at:
                    array.append(item)
            return array
