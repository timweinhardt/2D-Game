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
def generateChunk(num):
    for i in range(int(-num/2), int(num/2)):
        for j in range(int(-num/2), int(num/2)):
            new_tile_x = (config.SCREEN_WIDTH/2 - config.TILE_SIZE) + (j * config.TILE_SIZE)
            new_tile_y = (config.SCREEN_HEIGHT/2 - config.TILE_SIZE) + (i * config.TILE_SIZE)
            tile.add(Tile(choice(['grass-01', 'grass-02']), new_tile_x, new_tile_y))

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            generateChunk(16)

    screen.fill('#ffffff')
    tile.draw(screen)
    tile.update()
    player.update()
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)