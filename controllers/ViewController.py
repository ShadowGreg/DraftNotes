from core.BaseNote import BaseNote
from fileControllers.FileController import FileController
from view.Filter import Filter
from view.View import View
import logging


class ViewController:
    data = [BaseNote]
    start_msg = 'MENU'
    exit_msg = 'EXIT'
    logging.basicConfig(filename='./log/main.log', format='%(asctime)s -> %(message)s', encoding='utf-8',
                        level=logging.INFO)

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
            'DELETE': self.delete,
            'READ': self.read_note
        }

        while msg != self.exit_msg:

            key_list = list(menu_control.keys())
            key_list.append(self.exit_msg)

            if msg != 'EXIT':
                self.error_handling(menu_control[msg])

            self.view_tipe.select_command()
            msg = self.command_verification(key_list, input())

    def read_note(self):
        list_filter = Filter(self.core_tipe, self.read_data())
        self.view_tipe.search_note()
        id_note = str(input())

        id_note = self.search_for_single_note(id_note, list_filter)
        filtered_lis = list_filter.filter_id(id_note)
        print(self.text_formatter(filtered_lis[0].__repr__()))

    def text_formatter(self, msg: str):
        new_text = ''
        for i in range(len(msg)):
            new_text += msg[i]
            if i % 100 == 0:
                new_text += '\n'
        return new_text

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
        list_filter = Filter(self.core_tipe, self.read_data())
        self.view_tipe.list_filter()
        filter_date = str(input())

        if filter_date == '':
            self.data = list_filter.filter_data()
        else:
            self.data = list_filter.filter_data(filter_date)

        for item in self.data:
            print(item.get_short_text())
        self.data = None

    def edit(self):
        list_filter = Filter(self.core_tipe, self.read_data())
        self.view_tipe.search_note()
        id_note = str(input())

        id_note = self.search_for_single_note(id_note, list_filter)
        note = list_filter.get_one_note(id_note)
        self.view_tipe.title_note()
        new_title = str(input())
        self.view_tipe.body_note()
        new_body = str(input())
        self.data = list_filter.get_cleared_array(id_note)
        modify_note = note.modify(new_title, new_body)
        self.data.append(modify_note)
        self.write_data()

    def delete(self):
        list_filter = Filter(self.core_tipe, self.read_data())
        self.view_tipe.search_note()
        id_note = str(input())

        id_note = self.search_for_single_note(id_note, list_filter)

        self.data = list_filter.get_cleared_array(id_note)
        self.write_data()

    def search_for_single_note(self, id_note, list_filter):
        filtered_lis = list_filter.filter_id(id_note)
        while len(filtered_lis) > 1:
            self.view_tipe.some_notes_specify()
            self.print_for_search(filtered_lis)
            self.view_tipe.search_note()
            id_note = str(input())
            filtered_lis = list_filter.filter_id(id_note)
            if id_note == 'EXIT':
                self.run()
                pass
        return id_note

    def print_for_search(self, array: [BaseNote]):
        for item in array:
            print(item.get_text_for_search())

    def command_verification(self, keys: [], msg: str):
        msg = msg.upper()
        if msg in keys:
            return msg
        else:
            self.view_tipe.no_command()
            return self.start_msg

    def error_handling(self, command):
        try:
            command()
            logging.info(f'{str(command)}')
        except Exception as e:
            print(str(e))
            logging.error(f'{str(e)}')
