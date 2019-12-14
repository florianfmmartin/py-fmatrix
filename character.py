# character.py
# TODO: u"\u3400" a u"\u4fff"

# imports
from random import choice
from kanji import kanji_list
from tkinter import StringVar


class Character:
    # initialisation
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.kanji = StringVar()
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


if __name__ == "__main__":
    c = Character(0, 2)
    c.set_kanji()
    print(c.kanji)
