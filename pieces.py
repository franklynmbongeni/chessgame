class Piece:
    def __init__(self,type, color):
        self.type = type
        self.color = color

    def __str__(self):
        return f"{self.color} {self.type}"

class Pawn(Piece):
    def __init__(self,color):
        super().__init__("Pawn",color)
        self.has_moved = False

    def valid_moves(self,row , col, board ):
        moves = []

        """move straight ahead one square"""
        direction = -1 if self.color == "White" else 1

        new_row = row + direction

        if 0 <= new_row <= 7:
            if board[new_row][col] is None:
                moves.append((new_row,col))

                """to move two rows ahead"""
                if self.has_moved is False:
                    two_ahead = row + ( 2 * direction)
                    if board[two_ahead][col] is None:
                        moves.append((two_ahead,col))

            """Capture diagonally"""
        for col_offset in [-1, 1]:
            capture_col = col + col_offset
            if 0 <= capture_col <= 7 and 0 <= new_row <= 7:
                target = board[new_row][capture_col]
                if target is not None and target.color != self.color:
                    moves.append((new_row, capture_col))

        return moves


class Rook(Piece):
    def __init__(self,color):
        super().__init__("Rook",color)

    def valid_moves(self,row, col , board):
        moves = []


        """has a cross like movement"""
        offsets = [
            (-1,+0), (+1, +0), #up and down
            (+0,+1), (+0, -1) # left and right
            ]

        for row_offset, col_offset in offsets:
            new_row = row + row_offset
            new_col = col + col_offset

            while 0 <= new_row <= 7 and 0 <= new_col <= 7:
                if board[new_row][new_col] is None:
                    moves.append((new_row,new_col))
                elif board[new_row][new_col].color != self.color:
                    moves.append((new_row,new_col))
                    break
                else:
                    break
                new_row += row_offset
                new_col += col_offset


        return moves




class Knight(Piece):
    def __init__(self,color):
        super().__init__("Knight",color)

    def valid_moves(self,row , col,  board):
        moves = []

        """offsets co ordinates for knight movement """

        offsets = [
            (-2, -1), (-2, +1),  # up 2, left/right 1
            (+2, -1), (+2, +1),  # down 2, left/right 1
            (-1, -2), (-1, +2),  # up 1, left/right 2
            (+1, -2), (+1, +2)
        ]


        for row_offset , col_offset in offsets:
            new_row = row + row_offset
            new_col = col + col_offset

            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = board[new_row][new_col]
                if target is None or target.color != self.color:
                    moves.append((new_row,new_col))

        return moves



class Bishop(Piece):
    def __init__(self,color):
        super().__init__("Bishop",color)

    def valid_moves(self,row, col, board):
        moves = []

        offsets = [

            (-1, -1), (-1, +1), #up one row, left and right
            (+1, -1), (+1, +1) #down one row , left and right
        ]

        """trying to move to the right first"""
        for row_offset, col_offset in offsets:
            new_row = row + row_offset
            new_col = col + col_offset

            while 0 <= new_row <= 7 and 0 <= new_col <= 7:
                if board[new_row][new_col] is None:
                    moves.append((new_row,new_col))
                elif board[new_row][new_col].color != self.color: #the capture squares
                    moves.append((new_row,new_col))
                    break
                else:
                    break
                new_row += row_offset
                new_col += col_offset

        return moves







class Queen(Piece):
    def __init__(self,color):
        super().__init__("Queen",color)

    def valid_moves(self, row, col, board):
        moves = []

        """the rook and bishop movement all combined"""
        offsets = [
            (-1, 0), (+1, 0), (0, +1), (0, -1),  # rook
            (-1, -1), (-1, +1), (+1, -1), (+1, +1)  # bishop
        ]

        for row_offset, col_offset in offsets:
            new_row = row + row_offset
            new_col = col + col_offset
            while 0 <= new_row <= 7 and 0 <= new_col <= 7:
                if board[new_row][new_col] is None:
                    moves.append((new_row, new_col))
                elif board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
                new_row += row_offset
                new_col += col_offset

        return moves

class King(Piece):
    def __init__(self,color):
        super().__init__("King",color)

    def valid_moves(self,row, col , board):
        moves = []

        offsets = [
            (+1, -1), (+1,+0), (+1, +1),
            (+0, -1),          (+0, +1),
            (-1, -1), (-1, 0), (-1, +1)

        ]

        for row_offset, col_offset in offsets:
            new_row = row + row_offset
            new_col = col + col_offset
            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = board[new_row][new_col]
                if target is None or target.color != self.color:
                    moves.append((new_row, new_col))
        return moves


