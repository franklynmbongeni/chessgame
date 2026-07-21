from board import Board
from pieces import Pawn
from pieces import Rook

"""tests for the pawn"""
def test_pawn_moves_freely_on_empty_board():
    board = Board()
    pawn = Pawn("White")
    board.Grid[4][4] = pawn

    moves = pawn.valid_moves(4,4, board.Grid)

    assert (3,4) in moves #since it only moves one tile ahead"""

"""tests for the rook"""
def test_rook_moves_freely_on_empty_board():

    board = Board()
    rook = Rook("White")
    board.Grid[4][4] = rook

    moves = rook.valid_moves(4,4, board.Grid)

    assert (0, 4) in moves
    assert (7, 4) in moves
    assert (4, 0) in moves
    assert (4, 7) in moves

def test_rook_blocked_by_friendly_piece():

    board = Board()
    rook = Rook("White")
    blocker = Rook("White")
    board.Grid[4][4] = rook
    board.Grid[4][6] = blocker


    moves = rook.valid_moves(4,4, board.Grid)

    assert (4, 5) in moves  # can move up to the blocker
    assert (4, 6) not in moves  # can't capture own piece
    assert (4, 7) not in moves  # can't move past it

def test_rook_can_capture_enemy_piece():

    board = Board()
    rook = Rook("White")
    enemy_rook = Rook("Black")
    board.Grid[4][4] = rook
    board.Grid[4][6] = enemy_rook

    moves = rook.valid_moves(4,4, board.Grid)

    assert (4, 5) in moves #rook can move
    assert (4,6) in moves #rook can capture
    assert (4,7) not in moves # rook can't move past enemy piece





