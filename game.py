from piece import Piece, BLACK, WHITE
from pawn import Pawn
from queen import Queen
from knight import Knight
from bishop import Bishop
from rook import Rook
from king import King


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


def notation_to_coords(txt):
    abc = "abcdefgh"
    row0, col0 = int(txt.split("-")[0][0])-1, abc.index(txt.split("-")[0][1])
    row1, col1 = int(txt.split("-")[1][0])-1, abc.index(txt.split("-")[1][1])
    return row0, col0, row1, col1


def coords_to_notation(row0, col0, row1, col1):
    abc = "abcdefgh"
    return abc[col0]+str(row0+1)+"-"+abc[col1]+str(row1+1)

 
def print_board(board):
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.square(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def correct_coords(row, col):
    """The function checks if the coordinates (row, col) are inside the chessboard"""
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0][0] = Rook(0, 0, WHITE)
        self.field[0][7] = Rook(0, 7, WHITE)
        self.field[7][0] = Rook(7, 0, BLACK)
        self.field[7][7] = Rook(7, 7, BLACK)

        self.field[0][1] = Knight(0, 1, WHITE)
        self.field[0][6] = Knight(0, 6, WHITE)
        self.field[7][1] = Knight(7, 1, BLACK)
        self.field[7][6] = Knight(7, 6, BLACK)

        self.field[0][2] = Bishop(0, 2, WHITE)
        self.field[0][5] = Bishop(0, 5, WHITE)
        self.field[7][2] = Bishop(7, 2, BLACK)
        self.field[7][5] = Bishop(7, 5, BLACK)

        self.field[0][3] = Queen(0, 3, WHITE)
        self.field[0][4] = King(0, 4, WHITE)
        self.field[7][3] = Queen(7, 3, BLACK)
        self.field[7][4] = King(7, 4, BLACK)

        self.white = [self.field[0][0], self.field[0][7], self.field[0][1], self.field[0][6],
                                   self.field[0][2], self.field[0][5], self.field[0][3]]
        self.white_king = self.field[0][4]

        self.black = [self.field[7][0], self.field[7][7], self.field[7][1], self.field[7][6],
                                   self.field[7][2], self.field[7][5], self.field[7][3]]
        self.black_king = self.field[7][4]

        for i in range(0, 8):
            self.field[1][i] = Pawn(1, i, WHITE)
            self.white.append(self.field[1][i])

        for i in range(0, 8):
            self.field[6][i] = Pawn(6, i, BLACK)
            self.black.append(self.field[6][i])

    def current_player_color(self):
        return self.color

    def square(self, row, col):
        """Return a string with two characters for color and piece type (row, col) if the square is occupied and two spaces if the square is empty."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Move the piece from square (row, col) to square (row1, col1).
        Move and return True if the move is legal.
        Return False if the move is illegal."""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False 
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is not None and self.field[row1][col1].get_color() == piece.get_color():
            return False
        if not piece.can_move(row1, col1):
            return False
        if self.is_move_under_check(row, col, row1, col1):
            return False
        self.field[row][col] = None

        if self.color == WHITE and self.field[row1][col1] != None:
            self.black.remove(self.field[row1][col1])
        if self.color == BLACK and self.field[row1][col1] != None:
            self.white.remove(self.field[row1][col1])
        
        self.field[row1][col1] = piece 

        if isinstance(piece, Pawn) and piece.start_position and abs(row1-row) == 2:
            piece.start_position = False
        
        piece.set_position(row1, col1)
        self.color = opponent(self.color)

        return True
    
    def is_position_attacked(self, row1, col1):
        pieces_to_check = []
        if self.color == WHITE:
            pieces_to_check = self.black
        else:
            pieces_to_check = self.white
        for piece in pieces_to_check:
            if piece.can_move(row1, col1, self.field):
                return True
        return False
    
    def is_move_under_check(self, row, col, row1, col1):
        piece0 = self.field[row][col]
        piece1 = self.field[row1][col1]
        self.field[row][col] = None
        self.field[row1][col1] = piece0
        piece0.set_position(row1, col1)
        king: Piece = Piece(-1, -1, WHITE)
        if self.color == WHITE:
            king = self.white_king
        else:
            king = self.black_king
        is_king_checked = self.is_position_attacked(king.row, king.col)
        self.field[row][col] = piece0
        self.field[row1][col1] = piece1
        piece0.set_position(row, col)
        if is_king_checked:
            return True
        return False
 

def main():
    board = Board()
    while True:
        print_board(board)

        if board.current_player_color() == WHITE:
            print('White move:')
        else:
            print('Black move:')

        command = input()

        if command == 'exit':
            break
        
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Move successful')
        else:
            print('Coordinates incorrect. Try another move.')

if __name__  == "__main__":
    main()