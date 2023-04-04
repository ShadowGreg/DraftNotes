from core.BaseNote import BaseNote
import uuid
import datetime


class Note(BaseNote):
    def __init__(self, title: str, body: str):
        note_id = uuid.uuid4().__str__()
        note_created_at = datetime.datetime.now().strftime("%H-%M, %d %B, %Y").__str__()
        super().__init__(id=note_id, title=title, body=body, created_at=note_created_at, modified_at=None)

    def modify(self, title=None, body=None):
        self.title = title if title is not None else self.title
        self.body = body if body is not None else self.body
        self.modified_at = datetime.datetime.now().strftime("%H-%M, %d %B, %Y").__str__()

    def __str__(self):
        return super().__str__()

    def short_text(self):
        return super().short_text()
