from game import Game

def run_simulation():
    print("Initializing a new Chess game...")
    game = Game()
    
    print("\nInitial Board Layout:")
    game.board.print_board()
    
    # 1. White Pawn moves from (6, 3) to (4, 3) - Queen's Pawn Opening
    print("\n--- Move 1: White Pawn from (6, 3) to (4, 3) ---")
    game.attempt_move(6, 3, 4, 3)
    game.board.print_board()
    print(f"Current Turn: {game.current_turn}")
    
    # 2. Black Pawn moves from (1, 3) to (3, 3)
    print("\n--- Move 2: Black Pawn from (1, 3) to (3, 3) ---")
    game.attempt_move(1, 3, 3, 3)
    game.board.print_board()
    print(f"Current Turn: {game.current_turn}")

if __name__ == "__main__":
    run_simulation()
