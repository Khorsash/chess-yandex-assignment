from piece import Piece, WHITE, BLACK

class Pawn(Piece):
 
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.start_position = True
 
    def char(self):
        return 'P'

    def can_move(self, row1, col1, board):
        if super().can_move(row1, col1, board):
            if self.col != col1 and board[row1][col1] is not None:
                return True
            if self.col != col1 and board[row1][col1] is None:
                return False
            if board[row1][col1] is not None:
                return False
            if self.color == WHITE:
                direction = 1
                start_row = 1
            else:
                direction = -1
                start_row = 6

            if self.row + direction == row1:
                return True
    
            if self.row == start_row and self.row + 2 * direction == row1:
                return True
        return False