import pygame
from game import Game

pygame.init()

SQUARE_SIZE = 100
BOARD_SIZE = SQUARE_SIZE * 8

LIGHT = (235, 210, 183)
DARK = (160, 110, 80)

screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Chess")

game = Game()

def square_from_mouse():    #get the position of the click and convert it to board position
    x,y = pygame.mouse.get_pos()
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE

    return (row, col)

def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

font = pygame.font.SysFont("arial", 42, bold=True)

WHITE_PIECE = (250, 250, 250)
BLACK_PIECE = (20, 20, 20)

LABELS = {
    "Pawn": "P",
    "Rook": "R",
    "Knight": "N",
    "Bishop": "B",
    "Queen": "Q",
    "King": "K",
}


def draw_pieces():
    for row in range(8):
        for col in range(8):
            piece = game.board.get_piece(row, col)
            if piece is None:
                continue

            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            fill = WHITE_PIECE if piece.color == "White" else BLACK_PIECE
            pygame.draw.circle(screen, fill, center, SQUARE_SIZE // 2 - 10)

            label = LABELS[piece.type]
            text_color = BLACK_PIECE if piece.color == "White" else WHITE_PIECE
            text_surface = font.render(label, True, text_color)
            text_rect = text_surface.get_rect(center=center)
            screen.blit(text_surface, text_rect)

def main():
    running = True
    clock = pygame.time.Clock()
    selected_square = None

    """the first clicked is to select the piece on the square
                if piece exists we move to the second clicked will be for the destination square"""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked = square_from_mouse()

                if selected_square is None: #try to select piece
                    row , col = clicked
                    piece = game.board.get_piece(row, col)
                    if piece is not None and piece.color == game.current_turn:
                        selected_square = clicked
                else:
                    start_row, start_col = selected_square
                    end_row, end_col = clicked
                    attempt = game.attempt_move(start_row, start_col, end_row, end_col)
                    if attempt is True:
                        selected_square = None

        screen.fill((0, 0, 0))
        draw_board()
        draw_pieces()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()