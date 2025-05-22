from piece import Piece

# nije taj cuveni rook nego rock ali svakako
# https://i.ytimg.com/vi/Mw3jK9YwOxk/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGHIgSCg1MA8=&rs=AOn4CLADLNZ64XZMOhvfep-dTNe4ITNcBQ

class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def char(self):
        return "R"
    
    def possible_moves(self, board):
        pm = []
        return pm
    
    def figures_on_the_way(self, row1, col1, board):
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
            if self.row - row1 == 0 or self.col - col1 == 0:
                return True
        return False