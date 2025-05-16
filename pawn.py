from piece import Piece, WHITE, BLACK

class Pawn(Piece):
 
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
 
    def char(self):
        return 'P'
 
    def can_move(self, row, col):
        # Pawn can move only vertically
        # no en passant
        if self.col != col:
            return False
 
        # Pawn can move two squares forward from the starting position
        # so we put the start row index in start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
 
        # 1 square move
        if self.row + direction == row:
            return True
 
        # 2 square move from starting position
        if self.row == start_row and self.row + 2 * direction == row:
            return True
 
        return False