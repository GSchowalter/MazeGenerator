import pygame

#Initialize pygame
pygame.init()

#Initialize constants
game_width = 800
game_height = 400
screen_color = (8, 7, 97)

#Create screen
screen = pygame.display.set_mode((game_width,game_height))

#Title and icon
pygame.display.set_caption("Maze")

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Set display background
    screen.fill(screen_color)
    pygame.display.update()
