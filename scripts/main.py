#
# Import modules and classes
#
import pygame
import config
from sys import exit
from random import choice
from player import Player
from tile import Tile

#
# Initialize pygame and display window
#
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('2D Game')

#
# Sprite groups
#
player = pygame.sprite.GroupSingle()
player.add(Player())
tile = pygame.sprite.Group()

#
# Tile generation
#
for i in range(- 1, config.TILE_COLS + 1):
    for j in range(- 1, config.TILE_ROWS + 1):
        tile.add(Tile(choice(['grass-01', 'grass-02']), (config.TILE_SIZE * i,config.TILE_SIZE * j)))

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
    tile.draw(screen)
    tile.update()
    player.update()
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)