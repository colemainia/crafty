import board_square
class chessboard:
    def __init__(self, order=8):
        if order > 8: 
            raise ValueError('You can\'t make a chessboard bigger than 8x8.')
        self.order = order
        print('Chessboard of order ' + str(order) + ' initialized.')
