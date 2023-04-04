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
