from piece import Piece


def modulus(num):
    if num < 0:
        return num * -1
    return num


class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def char(self):
        return "Q"
    
    def can_move(self, row1, col1):
        if super().can_move(row1, col1):
            if modulus(self.row - row1) == modulus(self.col - col1) \
               or self.row - row1 == 0 or self.col - col1 == 0:
                return True
        return False