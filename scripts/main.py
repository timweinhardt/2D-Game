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
existing_tiles = set()

# Foreground tiles (ex. Rocks)
for i in range(10):
    y_pos = randint(0, config.TILE_ROWS)
    x_pos = randint(0, config.TILE_COLS)
    ForegroundTile('rock-01', (x_pos * config.TILE_SIZE, y_pos * config.TILE_SIZE), camera_group)

# Create tiles around player
def generate_background_tiles(x, y, distance_x, distance_y):
    player_grid_x = x // config.TILE_SIZE
    player_grid_y = y // config.TILE_SIZE
    for x in range(-distance_x, distance_x + 1):
        for y in range(-distance_y, distance_y + 1):
            tile_grid_x = player_grid_x + x
            tile_grid_y = player_grid_y + y
            # Check if there is a tile at this position
            if (tile_grid_x, tile_grid_y) not in existing_tiles:
                BackgroundTile(choice(['grass-01', 'grass-02']), (tile_grid_x * config.TILE_SIZE, tile_grid_y * config.TILE_SIZE), camera_group)
                existing_tiles.add((tile_grid_x, tile_grid_y))

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

    generate_background_tiles(player.position[0], player.position[1], config.TILE_COLS, config.TILE_ROWS)
    screen.fill('#ffffff')
    camera_group.update()
    camera_group.custom_draw(player)

    pygame.display.update()
    clock.tick(60)