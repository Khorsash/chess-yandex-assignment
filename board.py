from piece import Piece, BLACK, WHITE
from pawn import Pawn
from queen import Queen
from knight import Knight
from bishop import Bishop
from rock import Rock
from king import King
 

# Handy function for getting the opponent color
def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE
 

def print_board(board): # Print the board as a text
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
        # White pawn on the E2 square.
        self.field[1][4] = Pawn(1, 4, WHITE)  

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
            return False  # You cannot move to the same square
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Remove piece
        self.field[row1][col1] = piece  # Place the piece in another square
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True
 

def main():
    # Creating a chessboard
    board = Board()
    # Loop for player commands
    while True:
        # Display the position of pieces on the board
        print_board(board)
        # commands help
        print('Commands:')
        print('    exit                               -- exit')
        print('    move <row> <col> <row1> <col1>     -- move from square (row, col)')
        print('                                          to square (row1, col1)')
        # Invite the player of the correct color
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