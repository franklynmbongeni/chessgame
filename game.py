from board import Board
from pieces import Pawn


class Game:
    def __init__(self):
        self.board = Board()
        self.board.set_starting_position()
        self.current_turn = "White"
        self.selected_square = None

    def attempt_move(self, start_row, start_col, end_row, end_col):


        destination_square = (end_row, end_col)
        selected_piece = self.board.get_piece(start_row, start_col)
        if selected_piece:
            if selected_piece.color ==  self.current_turn:
                valid_moves = selected_piece.valid_moves(start_row, start_col,self.board.Grid)
                if destination_square in valid_moves: #then the move is valid
                    self.board.Grid[end_row][end_col] = selected_piece
                    self.board.Grid[start_row][start_col] = None
                    self.current_turn = "Black" if self.current_turn == "White" else "White"
                    if isinstance (selected_piece, Pawn):
                        selected_piece.has_moved = True

        else:
            """the move is invalid"""
            pass







