import pygame

class BackgroundTile(pygame.sprite.Sprite):
    def __init__(self, type, pos, group):
        super().__init__(group)
        if type == 'grass-01':
            self.image = pygame.image.load('assets/textures/tiles/grass-01.png').convert_alpha()
        elif type == 'grass-02':
            self.image = pygame.image.load('assets/textures/tiles/grass-02.png').convert_alpha()
        self.type = type
        self.position = pos
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft = pos)

class ForegroundTile(pygame.sprite.Sprite):
    def __init__(self, type, pos, group):
        super().__init__(group)
        if type == 'rock-01':
            self.image = pygame.image.load('assets/textures/tiles/rock-01.png').convert_alpha()
        self.type = type
        self.position = pos
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft = pos)