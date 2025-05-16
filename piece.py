WHITE = 1
BLACK = 2


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def can_move(self, row1, col1, board):
        return 0 <= row1 < 8 and 0 <= col1 < 8

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.color

    def char(self):
        return ""