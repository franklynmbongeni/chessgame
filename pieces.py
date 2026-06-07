class Piece:
    def __init__(self,type, color):
        self.type = type
        self.color = color

    def __str__(self):
        return f"{self.color} {self.type}"

class Pawn(Piece):
    def __init__(self,color):
        super().__init__("Pawn",color)

class Rook(Piece):
    def __init__(self,color):
        super().__init__("Rook",color)


class Knight(Piece):
    def __init__(self,color):
        super().__init__("Knight",color)

class Bishop(Piece):
    def __init__(self,color):
        super().__init__("Bishop",color)

class Queen(Piece):
    def __init__(self,color):
        super().__init__("Queen",color)

class King(Piece):
    def __init__(self,color):
        super().__init__("King",color)


