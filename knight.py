from piece import Piece


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def char(self):
        return "N"
    
    def possible_moves(self, board) -> list[tuple]:
        pm = []
        for i in [2, -2]:
            for j in [1, -2]:
                if self.can_move(self.row+i, self.col+j) and board[self.row+i][self.col+j].get_color() != self.color:
                    pm.append((i, j))
                if self.can_move(self.row+j, self.col+i) and board[self.row+j][self.col+i].get_color() != self.color:
                    pm.append((j, i))
        return pm
    
    def can_move(self, row1, col1, board):
        if super().can_move(row1, col1, board):
            if row1 >= 0 and row1 < 8 and col1 >= 0 and col1 < 8:
                if self.row - row1 in [-1, 1] and self.col - col1 in [-2, 2] \
                or self.row - row1 in [-2, 2] and self.col - col1 in [-1, 1]:
                    return True
        return False