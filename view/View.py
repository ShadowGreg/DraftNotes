from view import MenuText as mt


class View:

    @staticmethod
    def start():
        print(mt.start_menu)

    @staticmethod
    def select_command():
        print(mt.select_command)

    @staticmethod
    def add_title():
        print(mt.add_title)

    @staticmethod
    def add_body():
        print(mt.add_body)

    @staticmethod
    def note_list():
        print(mt.note_list)

    @staticmethod
    def no_command():
        print(mt.no_command)

    @staticmethod
    def list_filter():
        print(mt.list_filter)

    @staticmethod
    def search_note():
        print(mt.search_note)

    @staticmethod
    def some_notes_specify():
        print(mt.some_notes_specify)

    @staticmethod
    def title_note():
        print(mt.title_note)

    @staticmethod
    def body_note():
        print(mt.body_note)
