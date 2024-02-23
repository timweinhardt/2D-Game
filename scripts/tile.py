import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        if type == 'grass-01':
            texture = pygame.image.load('assets/textures/tiles/grass-01.png').convert_alpha()
        elif type == 'grass-02':
            texture = pygame.image.load('assets/textures/tiles/grass-02.png').convert_alpha()
        
        self.image = texture
        self.image = pygame.transform.scale_by(self.image, 4)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft = (x, y))
        self.player_speed = 3
    #
    # Player input listener
    #
    def player_input(self):
        keys = pygame.key.get_pressed()

        # Move tiles opposite to player movement
        if keys[pygame.K_w]:
            self.rect.y += self.player_speed
        elif keys[pygame.K_d]:
            self.rect.x -= self.player_speed
        elif keys[pygame.K_s]:
            self.rect.y -= self.player_speed
        elif keys[pygame.K_a]:
            self.rect.x += self.player_speed

    #
    # This method updates the tile information
    #
    def update(self):
        self.player_input()