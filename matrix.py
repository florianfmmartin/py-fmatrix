# matrix.py

# imports
import tkinter as tk
from time import sleep
from random import choice
from kanji import kanji_list


class Matrix:
    # initialisation
    def __init__(self):
        # window
        self.window = tk.Tk()
        self.window.title("py-fmatrix")
        self.width = 595
        self.height = 400
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.attributes('-type', 'dialog')

        # other params
        self.number_of_columns = 6
        self.full_opacity = 6
        self.random_columns = []
        self.frame = 1 / 10

        # single character size
        self.character_size_h = 16
        self.character_size_v = 19

        # list of possible positions
        self.pos_x = []
        self.pos_y = []
        for x in range(0, self.width // self.character_size_h):
            self.pos_x.append(x)
        for y in range(0, self.height // self.character_size_v):
            self.pos_y.append(y)
        self.last_row = self.pos_y[-1]

        # matrix of all characters
        self.characters = []
        for y in self.pos_y:
            row_list = []
            for x in self.pos_x:
                character_matrix = Character(x, y)
                row_list.append(character_matrix)
                character_matrix.kanji = tk.StringVar()
                character_matrix.set_kanji()
                character_matrix.label = tk.Label(self.window, text=character_matrix.kanji.get())
                character_matrix.label.grid(column=character_matrix.pos_x, row=character_matrix.pos_y)
            self.characters.append(row_list)

        # show window
        self.window.update()
        while True:
            sleep(0.1)
            chosen = self.characters[choice(self.pos_y)][choice(self.pos_x)]
            chosen.set_kanji()
            chosen.label.grid(column=chosen.pos_x, row=chosen.pos_y)
            self.window.update()

    def change_top_row(self):
        self.random_columns = []
        this_row = 0
        # what columns do i change
        for column in range(0, self.number_of_columns):
            self.random_columns.append(choice(self.pos_x))
        # for each of those columns
        for chosen_column in self.random_columns:
            chosen_character = self.characters[this_row][chosen_column]
            chosen_character.set_kanji()
            chosen_character.opacity = self.full_opacity

        # then we change next row
        self.change_next_row(self.random_columns, this_row)

        # sleep then change top
        sleep(1)
        self.change_top_row()

    def change_next_row(self, upper_random_columns, upper_row):
        current_row = upper_row + 1
        for column in upper_random_columns:
            self.characters[current_row][column].set_kanji()
            self.characters[current_row][column].opacity = self.full_opacity

        for column in upper_random_columns:
            up_row = upper_row
            for elements in range(0, self.full_opacity + 1):
                if self.characters[up_row][column].opacity != 0:
                    self.characters[up_row][column].opacity -= 1
                up_row -= 1

        if current_row != self.last_row:
            sleep(self.frame)
            self.change_next_row(upper_random_columns, current_row)


class Character(Matrix):
    # initialisation
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.kanji = tk.StringVar()
        self.label = None
        self.opacity = 6
        self.opacity_dict = {0: "#00d8dee9",
                             1: "#24d8dee9",
                             2: "#6bd8dee9",
                             3: "#8fd8dee9",
                             4: "#b3d8dee9",
                             5: "#d6d8dee9",
                             6: "#ffd8dee9",
                             }

    def set_kanji(self):
        self.kanji.set(choice(kanji_list))

