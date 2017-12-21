class board_square():
    """
    This class encapsulates all attributes of a
    single square in the board game 'Chess'.
    """
    def __init__(self, board_rank, board_file, piece=None):
        self.board_rank = board_rank  # The number or row
        self.board_file = board_file  # The column or letter
        self.piece = piece  # Specific chess piece
        self.dict_file_to_index = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7
        }

    def translate_file(self, board_file):
        """
        Translate the file into a 0 based numeric.

        Args: board_file (char): a-h column character
        Returns: file_index (int): 0-7 column integer
        Raise: Can raise KeyError when board_file not in dict
        """
        file_index = self.dict_file_to_index[board_file]
        return file_index
