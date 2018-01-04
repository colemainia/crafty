"""
The piece file includes all classes, enumerables, and
functionality that are needed to describe the particular
attributes and funtionality of each piece type in the
board game Chess.
"""
import board_square
import chessboard
from abc import ABC
from enum import Enum


class Color(Enum):
    """Enumerable with Color option Black or White."""
    BLACK = 0
    WHITE = 1


class Piece(ABC):
    """Abstract Base Class encapsulating piece color and move logic."""
    def __init__(self, color):
        self.color = color


class Rook(Piece):
    """The orthogonally moving Rook."""
    def __init__(self, color):
        self.relative_poss_coords = [
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0)
        ]
        super().__init__(color)


class Knight(Piece):
    """The 'L' moving Knight."""
    def __init__(self, color):
        self.relative_poss_coords = [
            (-2, 1), (-2, -1), (2, 1), (2, -1),
            (1, -2), (1, 2), (-1, 2), (-1, -2)
        ]
        super().__init__(color)


class Bishop(Piece):
    """The Diagonally moving Bishop."""
    def __init__(self, color):
        self.relative_poss_coords = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
            (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
            (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
            (-1, -1), (-2, -2), (-3, -3), (-4, -4),
            (-5, -5), (-6, -6), (-7, -7)
        ]
        super().__init__(color)


class Pawn(Piece):
    """The Forward moving Pawn."""
    def __init__(self, color):
        self.relative_poss_coords = [
            (0, 1), (0, 2), (1, 1), (-1, 1)
        ]
        super().__init__(color)


class King(Piece):
    """The Single square moving King."""
    def __init__(self, color):
        self.relative_poss_coords = [
            (0, 1), (1, 1), (1, 0), (1, -1),
            (0, -1), (-1, -1), (-1, 0), (-1, 1)
        ]
        super().__init__(color)
