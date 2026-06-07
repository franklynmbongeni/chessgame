from pieces import Rook, Knight, Bishop, Queen, King, Piece , Pawn


class Board:
    def __init__(self):

        self.Grid = [[None for _ in range(8)] for _ in range(8)]



    def set_starting_position(self):

        """for the black pieces"""
        for i in range(8):
            self.Grid[1][i] = Pawn("Black")

        self.Grid[0][0] = Rook("Black")
        self.Grid[0][7] = Rook("Black")

        self.Grid[0][1] = Knight("Black")
        self.Grid[0][6] = Knight("Black")

        self.Grid[0][2] = Bishop("Black")
        self.Grid[0][5] = Bishop("Black")

        self.Grid[0][3] = Queen("Black")
        self.Grid[0][4] = King("Black")

        """for the white pieces"""
        for i in range(8):
            self.Grid[6][i] = Pawn("White")

        self.Grid[7][0] = Rook("White")
        self.Grid[7][7] = Rook("White")

        self.Grid[7][1] = Knight("White")
        self.Grid[7][6] = Knight("White")

        self.Grid[7][2] = Bishop("White")
        self.Grid[7][5] = Bishop("White")

        self.Grid[7][3] = Queen("White")
        self.Grid[7][4] = King("White")



    """temporary function to check grid"""
    def print_board(self):
        for row in self.Grid:
            print([str(piece) if piece is not None else None for piece in row])



dummy = Board()
dummy.set_starting_position()
dummy.print_board()