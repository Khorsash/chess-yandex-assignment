from piece import Piece


def modulus(num):
    if num < 0:
        return num * -1
    return num


class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def char(self):
        return "K"
    
    def can_move(self, row1, col1):
        if super().can_move(row1, col1):
            if 0 <= modulus(row1-self.row) <= 1 and 0 <= modulus(col1-self.col) <= 1:
                return True
        return False