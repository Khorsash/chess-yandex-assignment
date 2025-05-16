from piece import Piece


def modulus(num):
    if num < 0:
        return num * -1
    return num


class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def char(self):
        return "B"
    
    def can_move(self, row1, col1):
        if super().can_move(row1, col1):
            if modulus(self.row - row1) == modulus(self.col - col1):
                return True
        return False