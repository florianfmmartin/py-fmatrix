# matrix.py

# imports
import tkinter as tk
from character import Character
from time import sleep


class Matrix:
    # initialisation
    def __init__(self):
        # window
        self.window = tk.Tk()
        self.window.title("py-fmatrix")
        self.width = 600
        self.height = 400
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.attributes('-type', 'dialog')

        # single caracter size
        self.caracter_size_h = 10
        self.caracter_size_v = 40

        # matrix of all caracters
        self.caracters = []
        for pos_y in range(0, self.height // self.caracter_size_v):
            row_list = []
            for pos_x in range(0, self.width // self.caracter_size_h):
                row_list.append(Character(pos_x, pos_y))
            self.caracters.append(row_list)

        # infinite loop
        while True:
            sleep(0.05)
            self.change_top_row()

    def change_top_row(self):
        self.change_top_row_kanji()
        self.change_top_row_opacity()
        self.change_next_row()
        pass

    def change_top_row_kanji(self):
        pass

    def change_top_row_opacity(self):
        pass

    def change_next_row(self):
        # if next row is last pass
        pass
