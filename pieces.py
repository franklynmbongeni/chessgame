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
                moves.append([new_row,col])

                """to move two rows ahead"""
            if self.has_moved is False:
                two_ahead = row + ( 2 * direction)
                if board[two_ahead][col] is None:
                    moves.append([two_ahead,col])

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

        """up"""
        r = row + 1
        while r <= 7:
            if board[r][col] is None:
                moves.append([r,col])
            if board[r][col] != self.color:
                moves.append([r,col])
                break
            else:
                break
            r += 1

        """down: this from whites view will be moving up the board """
        r = row - 1
        while r >= 0:
            if board[r][col] is None:
                moves.append([r,col])
            if board[r][col] != self.color:
                moves.append([r,col])
                break
            else:
                break

            r -= 1

        """right"""
        c = col + 1
        while c <= 7:
            if board[row][c] is None:
                moves.append([row,c])
            if board[row][c] != self.color:
                moves.append([row,c])
                break
            else:
                break
            c += 1


                c += 1

        """left"""
        c = col - 1
        while c >= 0:
            if board[row][c] is None:
                moves.append([row,c])
            if board[row][c] != self.color:
                moves.append([row,c])
                break
            else:
                break
            c -= 1



class Knight(Piece):
    def __init__(self,color):
        super().__init__("Knight",color)

    def valid_moves(self,row , col,  board):
        moves = []

        

class Bishop(Piece):
    def __init__(self,color):
        super().__init__("Bishop",color)

class Queen(Piece):
    def __init__(self,color):
        super().__init__("Queen",color)

class King(Piece):
    def __init__(self,color):
        super().__init__("King",color)


