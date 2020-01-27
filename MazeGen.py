import pygame

#Initialize pygame
pygame.init()

#Initialize constants
game_width = 800
game_height = 400

#Create screen
screen = pygame.display.set_mode((game_width,game_height))

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False