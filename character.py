# character.py
# TODO: u"\u3400" a u"\u4fff"


class Character:
    # initialisation
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.kanji = u""
        self.opacity = 0
