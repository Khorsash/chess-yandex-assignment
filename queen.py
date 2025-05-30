from piece import Piece


class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def char(self):
        return "Q"
    
    def possible_moves(self, board):
        pm = []
        for i in range(8):
            if board[self.row][i] is None or board[self.row][i].get_color() != self.color:
                pm.append((self.row, i))
            if board[i][self.col] is None or board[i][self.col].get_color() != self.color:
                pm.append((i, self.col))
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
        if self.row - row1 == 0:
            step = (col1-self.col)/abs(col1-self.col)
            for i in range(self.col+1, col1, step):
                if board[self.row][i] is not None:
                    return True
        if self.col - col1 == 0:
            step = (row1-self.row)/abs(col1-self.col)
            for i in range(self.row+1, row1, step):
                if board[i][self.col] is not None:
                    return True
        return False
    
    def can_move(self, row1, col1, board):
        if super().can_move(row1, col1, board) and not self.figures_on_the_way(row1, col1, board):
            if abs(self.row - row1) == abs(self.col - col1) \
               or self.row - row1 == 0 or self.col - col1 == 0:
                return True
        return False