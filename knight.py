from piece import Piece


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def char(self):
        return "N"
    
    def can_move(self, row1, col1):
        if row1 >= 0 and row1 < 8 and col1 >= 0 and col1 < 8:
            if self.row - row1 in [-1, 1] and self.col - col1 in [-2, 2] \
               or self.row - row1 in [-2, 2] and self.col - col1 in [-1, 1]:
                return True
        return False