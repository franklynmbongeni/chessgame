 chess game
# ♟️ Python Chess

A chess engine and GUI built from scratch in Python — no external chess libraries, just object-oriented design and pygame for rendering.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![pygame](https://img.shields.io/badge/pygame-2.x-green)
![Tests](https://img.shields.io/badge/tests-pytest-yellow)

## Features

- **Full piece movement logic** — Pawn (including double-step and diagonal captures), Rook, Knight, Bishop, Queen, and King, each implemented as its own class with its own `valid_moves` logic.
- **Turn-based play** — alternates White/Black automatically and rejects moves that are out of turn or illegal.
- **Check detection** — scans the board to determine whether a given player's king is currently under attack.
- **Interactive GUI** — click-to-select, click-to-move board rendered with pygame, with legal move highlighting.
- **Unit tested** — core piece movement rules are covered with `pytest`.

## Project structure

```
chess/
├── pieces.py        # Piece base class + Pawn, Rook, Knight, Bishop, Queen, King
├── board.py         # Board state, starting position, find_king, is_in_check
├── game.py          # Game class: turn management, move validation, attempt_move
├── main.py          # pygame GUI — click-to-move interface
├── simulation.py     # scripted demo game (no GUI, prints board to console)
├── test_pieces.py   # pytest suite for piece movement rules
└── README.md
```

## Getting started

### Requirements

```
pip install pygame pytest
```

### Run the GUI

```
python main.py
```

Click a piece to select it (legal moves are highlighted), then click a destination square to move.

### Run the console simulation

```
python simulation.py
```

Prints the board to the terminal after each scripted move — useful for debugging game logic without the GUI.

### Run the tests

```
pytest -v
```

## Roadmap

- [ ] Prevent moves that leave your own king in check
- [ ] Checkmate / stalemate detection
- [ ] Castling
- [ ] En passant
- [ ] Pawn promotion
- [ ] Move history / algebraic notation display

## Why I built this

A from-scratch chess engine touches a lot of core CS ground at once: object-oriented design (inheritance and polymorphism across piece types), 2D grid/coordinate logic, game-state management, and eventually more involved rule-checking (check/checkmate) that ties movement, board state, and turn logic together. It's also just a genuinely fun project to debug — the rules are precise enough that bugs are obvious once you see them, but subtle enough to actually make you think.

## License

MIT — do whatever you want with it. 

AUTHOR

Mbongeni Franklyn Ngwenya
