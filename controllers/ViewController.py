from core.BaseNote import BaseNote
from fileControllers.FileController import FileController
from view.View import View


class ViewController:
    data = [BaseNote]
    start_msg = 'MENU'
    exit_msg = 'EXIT'

    def __init__(self, view_tipe: View, core_tipe: BaseNote, file_tipe: FileController):
        self.view_tipe = view_tipe
        self.file_tipe = file_tipe
        self.core_tipe = core_tipe

    def run(self, msg=start_msg):
        menu_control = {
            'MENU': self.menu,
            'ADD': self.add,
            'LIST': self.list,
            'EDIT': self.edit,
            'DELETE': self.delete
        }

        while msg != self.exit_msg:

            key_list = list(menu_control.keys())
            key_list.append(self.exit_msg)

            if msg != 'EXIT':
                menu_control[msg]()

            self.view_tipe.select_command()
            msg = self.command_verification(key_list, input())

    def read_data(self):
        return self.file_tipe.read()

    def write_data(self):
        return self.file_tipe.write(self.data)

    def menu(self):
        self.view_tipe.start()

    def add(self):
        self.data = self.read_data()
        note = self.core_tipe(self.input_title(), self.input_body())
        self.data.append(note)
        self.write_data()
        self.data = None

    def input_title(self):
        self.view_tipe.add_title()
        return input()

    def input_body(self):
        self.view_tipe.add_body()
        return input()

    def list(self):
        self.data = self.read_data()
        for item in self.data:
            print(item.short_text())
        self.data = None

    def edit(self):
        pass

    def delete(self):
        pass

    def command_verification(self, keys: [], msg: str):
        msg = msg.upper()
        if msg in keys:
            return msg
        else:
            self.view_tipe.no_command()
            return self.start_msg
