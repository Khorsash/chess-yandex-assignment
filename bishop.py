from piece import Piece


class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def char(self):
        return "B"
    
    def possible_moves(self, board) -> list[tuple]:
        pm = []

        for l in [1, -1]:
            for k in [1, -1]:
                i, j = self.row+l, self.col+k
                while self.can_move(i, j, board):
                    if board[i][j] is not None and board[i][j].get_color() == self.color:
                        break
                    if board[i][j] is not None and board[i][j].get_color() != self.color:
                        pm.append((i, j))
                        break
                    pm.append((i, j))
                    i += l
                    j += k
        return pm

    def figures_on_the_way(self, row1, col1, board):
        if abs(row1-self.row) == abs(self.col - col1):
            step = (row1-self.row)/abs(row1-self.row)
            for i in range(1, abs(row1-self.row), step):
                if board[self.row+i*step][self.col+i*step] is not None:
                    return True
        return False
    
    def can_move(self, row1, col1, board):
        if super().can_move(row1, col1, board):
            if abs(self.row - row1) == abs(self.col - col1):
                return True
        return False