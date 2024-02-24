import pygame
from tile import BackgroundTile
import config

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        self.delay = 0.07

    #
    # Update camera offset based on target's (ex. player) position
    #
    def center_target_camera(self, target):
        self.offset.x += (target.rect.centerx - (self.half_w + self.offset.x)) * self.delay
        self.offset.y += (target.rect.centery - (self.half_h + self.offset.y)) * self.delay

    #
    # Draw background and foreground tiles
    #
    def custom_draw(self, player):
        self.center_target_camera(player)
        # Background Tiles
        for sprite in self.sprites():
            background_offset = sprite.rect.topleft - self.offset
            if isinstance(sprite, BackgroundTile):
                self.display_surface.blit(sprite.image, background_offset)
        # Draw foreground tiles by sorting each tile by its y position
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            foreground_offset = sprite.rect.topleft - self.offset
            if not isinstance(sprite, BackgroundTile):
                self.display_surface.blit(sprite.image, foreground_offset)