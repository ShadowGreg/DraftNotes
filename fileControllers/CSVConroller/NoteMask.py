import core.BaseNote as Note


class NoteMask:
    title = ''
    body = ''
    id = ''
    created_at = ''
    modified_at = ''

    def __init__(self, note_class: Note.BaseNote):
        self.title = note_class.title
        self.body = note_class.body
        self.id = note_class.id
        self.created_at = note_class.created_at
        self.modified_at = note_class.modified_at

    @staticmethod
    def make_base_note(array: []):
        return Note.BaseNote(in_id=array[0], title=array[1], body=array[2], created_at=array[3], modified_at=array[4])
