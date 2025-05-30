from piece import Piece


class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def char(self):
        return "K"
    
    def possible_moves(self, board):
        pm = []
        for i in [1, 0, -1]:
            for j in [1, 0, -1]:
                if self.can_move(self.row+i, self.col+j, board) and board[self.row+i][self.col+j].get_color() != self.color:
                    pm.append((self.row+i, self.col+j))
        pm.remove((self.row, self.col))
        return pm
    
    def can_move(self, row1, col1, board):
        if super().can_move(row1, col1, board):
            if 0 <= abs(row1-self.row) <= 1 and 0 <= abs(col1-self.col) <= 1:
                return True
        return False