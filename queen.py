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
    
    def figures_on_the_way(self, row1, col1, board):
        if modulus(row1-self.row) == modulus(self.col - col1):
            step = (row1-self.row)/modulus(row1-self.row)
            for i in range(1, modulus(row1-self.row), step):
                if board[self.row+i*step][self.col+i*step] is not None:
                    return True
        if self.row - row1 == 0:
            step = (col1-self.col)/modulus(col1-self.col)
            for i in range(self.col+1, col1, step):
                if board[self.row][i] is not None:
                    return True
        if self.col - col1 == 0:
            step = (row1-self.row)/modulus(col1-self.col)
            for i in range(self.row+1, row1, step):
                if board[i][self.col] is not None:
                    return True
        return False
    
    def can_move(self, row1, col1, board):
        if super().can_move(row1, col1, board) and not self.figures_on_the_way(row1, col1, board):
            if modulus(self.row - row1) == modulus(self.col - col1) \
               or self.row - row1 == 0 or self.col - col1 == 0:
                return True
        return False