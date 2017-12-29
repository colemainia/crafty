import board_square
import chessboard
import piece
import unittest

testboard = chessboard.Chessboard().squares
test_rook = piece.Rook(piece.Color.WHITE)
testboard[7][1].piece = test_rook


class TestBoardSquares(unittest.TestCase):
    """
    This unit test tests the chessboard and its squares.
    """
    def test_71(self):
        self.assertEqual(testboard[7][1].board_file, 7)
        self.assertEqual(testboard[7][1].board_rank, 1)
        self.assertEqual(testboard[7][1].piece, test_rook)

    def test_size(self):
        self.assertEqual(len(testboard), 8)
        self.assertEqual(len(testboard[0]), 8)


class TestRookMoves(unittest.TestCase):
    """
    This unit test tests a White Rook standing on g7.
    """
    def test_rook_color(self):
        self.assertEqual(test_rook.color, piece.Color.WHITE)

    def test_rook_moves(self):
        pass


if __name__ == '__main__':
    unittest.main()
