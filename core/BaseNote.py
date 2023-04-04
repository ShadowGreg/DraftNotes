class BaseNote:
    end_id_index = 8
    id = None
    title = None
    body = None
    created_at = None
    modified_at = None

    def __init__(self, in_id: str, title: str, body: str, created_at: str, modified_at: str):
        self.id = in_id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.modified_at = modified_at

    def __str__(self):
        if self.modified_at is not None:
            return f"\nNote {self.id[0:8]}: {self.title}\n{self.body}\nCreated at: {self.created_at}\nLast modified at: {self.modified_at}\n"
        return f"\nNote {self.id[0:8]}: {self.title}\n{self.body}\nCreated at: {self.created_at}\n"

    def __repr__(self):
        return self.__str__()

    def get_short_text(self):
        end_index = 30
        return f"\nNote {self.id[0:8]}: {self.title}\n{self.body[0:end_index]}\nCreated at: {str(self.created_at)}\n"

    def get_text_for_search(self):
        end_index = 30
        return f"\nNote {self.id}\n Title: {self.title}\n{self.body[0:end_index]}\nCreated at: {str(self.created_at)}\n"

    def __lt__(self, other):
        return self.created_at < other.created_at

