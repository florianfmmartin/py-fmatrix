# imports
import tkinter as tk
from random import choice
from time import sleep
from kanji import kanji_list


class Matrix:
    # init
    def __init__(self):
        # init
        self.window = tk.Tk()
        self.window.title("py-fmatrix")
        self.width = 600
        self.height = 400
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.attributes("-type", "dialog")
        self.char_size_x = 16
        self.char_size_y = 19
        self.chars = []
        self.x_list = []
        self.y_list = []
        self.last_row = self.height // self.char_size_y
        self.five_last = [self.last_row - 5, self.last_row - 4, self.last_row - 3, self.last_row - 2, self.last_row - 1, self.last_row]
        self.init_chars()
        self.top_row_numb = 3

        # loop
        self.window.bind("<Return>", self.start)
        self.window.geometry(f"{self.width}x{self.height - (5 * self.char_size_y)}")
        self.window.mainloop()

    def init_chars(self):
        for x in range(0, self.width // self.char_size_x):
            self.x_list.append(x)
        for y in range(0, self.height // self.char_size_y):
            self.y_list.append(y)

        for x in self.x_list:
            column_list = []
            for y in self.y_list:
                char = Char(x, y, self)
                column_list.append(char)
            self.chars.append(column_list)

    def start(self, event):
        # print(f"hit -- {event}")
        self.top_row()
        sleep(0.06)
        self.char_scan()
        self.window.update()
        self.start(None)

    def top_row(self):
        top_row_list = []
        for x in self.x_list:
            char_of_top = self.chars[x][0]
            if char_of_top.opacity == 6:
                top_row_list.append(char_of_top)

        if len(top_row_list) < self.top_row_numb:
            for times in range(0, self.top_row_numb - len(top_row_list)):
                rand_top_char = self.chars[choice(self.x_list)][0]
                rand_top_char.opacity = 6
                rand_top_char.set_kanji()
                rand_top_char.set_opacity()

    def char_scan(self):
        char_on_screen = []
        for x in self.x_list:
            for y in self.y_list:
                char = self.chars[x][y]
                if char.opacity == 6:
                    char_on_screen.append(char)

        for char in char_on_screen:
            self.char_change(char.pos_x, char.pos_y)


    def char_change(self, x, y):
        try:
            next_char = self.chars[x][y+1]
            next_char.set_kanji()
            next_char.opacity = 6
            next_char.set_opacity()
        except:
            # print("n")
            pass

        try:
            present_char = self.chars[x][y]
            present_char.opacity -= 1
            present_char.set_opacity()
        except:
            # print("p")
            pass

        for upper in range(1, 6):
            try:
                if y - upper >= 0:
                    up_char = self.chars[x][y - upper]
                    if up_char.opacity > 0:
                        up_char.opacity -= 1
                    up_char.set_opacity()
            except:
                # print("u")
                pass


class Char:
    # init
    def __init__(self, x, y, master):
        self.pos_x = x
        self.pos_y = y
        self.master = master
        self.kanji = "罪"
        self.opacity = 0
        self.dict = {0: "#282828",
                     1: "#3C3836",
                     2: "#504945",
                     3: "#665C54",
                     4: "#7C6F64",
                     5: "#928374",
                     6: "#EBDBB2"}
        self.label = tk.Label(self.master.window, text=self.kanji, fg="#A3BE8C")
        if self.pos_y not in self.master.five_last:
            self.label.grid(column=self.pos_x, row=self.pos_y)
        self.set_kanji()
        self.set_opacity()

    def set_kanji(self):
        self.kanji = choice(kanji_list)
        self.label["text"] = self.kanji

    def set_opacity(self):
        self.label["fg"] = self.dict[self.opacity]
