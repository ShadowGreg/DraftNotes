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

    def filter_id(self, input_id: str):
        array = []
        for item in self.array:
            if input_id in item.id:
                array.append(item)
        return array

    def get_cleared_array(self, input_id: str):
        array = []
        for item in self.array:
            if input_id not in item.id:
                array.append(item)
        return array
