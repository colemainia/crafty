# Chess board square
# Coleman A. Hoyt
class board_square():
    # ctor: called by board, sets rank and file, possibly piece
    def __init__(self, board_rank, board_file, piece = None):
        self.board_rank = board_rank
        self.board_file = board_file
        self.piece = piece

    def get_coordinates(self):
        return (self.board_file, self.board_rank)

    def get_piece(self):
        return self.piece

    def set_piece(self, new_piece):
        self.piece = new_piece
