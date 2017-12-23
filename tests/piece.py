import chessboard
import board_square
from abc import ABC
from enum import Enum

"""
DEVELOPMENT DOCSTRING: ROADMAP
The chess pieces will first be tested for controlling squares. We will begin
with pieces which I feel are simple and finish with ones which are 
complicated. They are scheduled to be implemented in this order, from least
to most complicated: Rook, Bishop, Queen, King, Knight, and Pawn. Pawns have
multiple special rules, accordingly, its implementation will remain "fuzzy"
until the end of these tests. Once conrolling squares is finished, allowed
moves will be implemented.
"""
class Color(Enum):
    """
    The 'Color' class implements the enumerable colors that a chess piece 
    may have. That is, a chess piece is either Black or White.
    """
    BLACK = 1
    WHITE = 2

class Piece(ABC):
    """
    the 'Piece' class implements all of the attributes of a chess piece. 
    It is an abstract base class with abstract methods.
    """
    def __init__(self, color, square):
        self.color = color
        self.square = square
        square.piece = self

    def controlled_squares(self, board):
        """
        the 'controlled_squares' method returns the set of squares which the
        piece attacks.
        """
        pass

    def allowed_moves(self, board):
        """
        the 'allowed_moves' method returns the set of squares which the 
        piece may move to. This usually a subset of 'controlled_squares'; 
        exceptions are Pawns, and Kings and Rooks that may castle.
        """
        pass


class Rook(Piece):
    """
    The 'Rook' class implements all of the attributes of a Black or White
    Rook in the game of chess. It is a child of the parent abstract class
    'Piece'.  It can move to any unobstructed square on its orthogonal axes.
    It may also "castle" with its King of the same color. Rules on castling
    are contained in the 'King' class, since castling is considered two
    separate moves played on the same turn, beginning with the King's move.
    """
    pass
