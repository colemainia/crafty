import chessboard
import board_square
from abc import ABC
from enum import Enum


"""
DOCSTRING: A SUGGESTION FOR CO-PILOT

I think a good idea for this, in addition to your plan, is to
break up the move rules into types, such as orthogonal, diagonal,
king's, pawn's, and knight's. That way, rules like orthogonal
and diagonal are not defined twice for each piece that uses them.
This also would make our project more readable.
"""
class Color(Enum):
    """
    This Enumerable encapsulates the two colors that a Piece may have.
    That is, a chess piece is either Black or White.
    """
    BLACK = 1
    WHITE = 2

class Piece(ABC):
    """
    This Abstract Base Class encapsulates all of the attributes of a single
    piece in the game of 'Chess'.
    """
    def __init__(self, color):
        self.color = color


class Rook(Piece):
    """
    This Piece encapsulates all of the attributes of a Black or White
    Rook in the game of 'Chess'. It moves orthogonally.
    """
    pass
