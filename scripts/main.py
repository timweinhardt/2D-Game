#
# Import modules and classes
#
import pygame
from sys import exit
from player import Player

#
# Define any constants
#
TILE_SIZE = 64
SCREEN_WIDTH = TILE_SIZE * 12
SCREEN_HEIGHT = TILE_SIZE * 7

#
# Initialize pygame and display window
#
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('2D Game')

#
# Sprite groups
#
player = pygame.sprite.GroupSingle()
player.add(Player())

#
# Timers
#
clock = pygame.time.Clock()

#
# Game loop
#
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('#ffffff')
    player.update()
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)