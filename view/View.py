from view import MenuText as mt


class View:
    def start(self):
        msg = ''
        while msg != 'EXIT':
            print(mt.start_menu)
            msg = input().upper()
