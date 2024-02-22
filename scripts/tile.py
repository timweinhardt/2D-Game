import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, type, position):
        super().__init__()
        if type == 'grass-01':
            texture = pygame.image.load('assets/textures/tiles/grass-01.png').convert_alpha()
        elif type == 'grass-02':
            texture = pygame.image.load('assets/textures/tiles/grass-02.png').convert_alpha()
        
        self.image = texture
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft = position)
        self.player_speed = 3
    #
    # Player input listener
    #
    def player_input(self):
        keys = pygame.key.get_pressed()
        speed_modifier = 1
        num_keys_pressed = sum(1 for key in keys if key)

        # Move tiles opposite to player movement
        # Reduce speed if the player is moving diagonally
        if (num_keys_pressed > 1):
            speed_modifier = 1.41
        if keys[pygame.K_w]:
            self.rect.y += self.player_speed/speed_modifier
        if keys[pygame.K_d]:
            self.rect.x -= self.player_speed/speed_modifier
        if keys[pygame.K_s]:
            self.rect.y -= self.player_speed/speed_modifier
        if keys[pygame.K_a]:
            self.rect.x += self.player_speed/speed_modifier

    #
    # This method updates the tile information
    #
    def update(self):
        self.player_input()