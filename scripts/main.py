#
# Import modules and classes
#
import pygame
import config
from sys import exit
from random import choice, randint
from player import Player
from camera import CameraGroup
from tile import BackgroundTile, ForegroundTile

#
# Initialize pygame and display window
#
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('2D Game')

#
# Sprite groups
#
camera_group = CameraGroup()
player = Player((config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2), camera_group)

#
# Tile generation
#

# Background tiles (ex. Grass)
for i in range(config.TILE_ROWS):
    for j in range(config.TILE_COLS):
        BackgroundTile(choice(['grass-01', 'grass-02']), (j * config.TILE_SIZE, i * config.TILE_SIZE), camera_group)

# Foreground tiles (ex. Rocks)
for i in range(3):
    y_pos = randint(0, config.TILE_ROWS)
    x_pos = randint(0, config.TILE_COLS)
    ForegroundTile('rock-01', (x_pos * config.TILE_SIZE, y_pos * config.TILE_SIZE), camera_group)

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
    camera_group.update()
    camera_group.custom_draw(player)

    pygame.display.update()
    clock.tick(60)