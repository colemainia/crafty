import board_square
ORDER = 8
class Chessboard:
    """
    This class encapsulates all the attributes of a board
    in the game of 'Chess'.
    """
    def __init__(self):
        self.squares = [[] for i in range(ORDER)]
        for board_file, row in enumerate(self.squares):
            for board_rank in range(ORDER):
                row.append(board_square.BoardSquare(board_rank, board_file))

        print('Chessboard of order ' + str(ORDER) + ' initialized.')

