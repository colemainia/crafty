import unittest
import board_square
import chessboard

testboard = chessboard.chessboard().squares

class TestBoardSquares(unittest.TestCase):
    """
    This unit test tests the chessboard and its squares.
    """
    def test_71(self):
        self.assertEqual(testboard[7][1].board_file, 7)
        self.assertEqual(testboard[7][1].board_rank, 1)
        
    def test_size(self):
        self.assertEqual(len(testboard), 8)
        self.assertEqual(len(testboard[0]), 8)

if __name__ == '__main__':
    unittest.main()
