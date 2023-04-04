from core.BaseNote import BaseNote
import uuid
import datetime


class Note(BaseNote):
    def __init__(self, title: str, body: str):
        note_id = uuid.uuid4().__str__()
        note_created_at = datetime.datetime.now().strftime("%H-%M, %d %B, %Y").__str__()
        super().__init__(in_id=note_id, title=title, body=body, created_at=note_created_at, modified_at=None)

    def __str__(self):
        return super().__str__()

    def get_short_text(self):
        return super().get_short_text()
