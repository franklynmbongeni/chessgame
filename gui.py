import pygame

#this is code is not used at the moment i have to complete the game logic 

pygame.init()

square_size = 100
screen = pygame.display.set_mode((1000,888))
pygame.display.set_caption("Chess")

running = True
while running:
    # 1. Event checking loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Fill the screen with color
    screen.fill((255, 0, 255))

    # 3. Update the display to show the changes
    pygame.display.flip()

# Outside the loop: quit pygame
pygame.quit()

pygame.quit()


