import pygame
import config

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        front_1 = pygame.image.load('assets/textures/player/front-01.png').convert_alpha()
        front_2 = pygame.image.load('assets/textures/player/front-02.png').convert_alpha()
        front_3 = pygame.image.load('assets/textures/player/front-03.png').convert_alpha()

        right_1 = pygame.image.load('assets/textures/player/right-01.png').convert_alpha()
        right_2 = pygame.image.load('assets/textures/player/right-02.png').convert_alpha()
        right_3 = pygame.image.load('assets/textures/player/right-03.png').convert_alpha()

        back_1 = pygame.image.load('assets/textures/player/back-01.png').convert_alpha()
        back_2 = pygame.image.load('assets/textures/player/back-02.png').convert_alpha()
        back_3 = pygame.image.load('assets/textures/player/back-03.png').convert_alpha()

        left_1 = pygame.image.load('assets/textures/player/left-01.png').convert_alpha()
        left_2 = pygame.image.load('assets/textures/player/left-02.png').convert_alpha()
        left_3 = pygame.image.load('assets/textures/player/left-03.png').convert_alpha()

        self.player_walk = [[front_1, front_2, front_3],[right_1, right_2, right_3],[back_1, back_2, back_3],[left_1, left_2, left_3]]
        self.frame_index = 0
        self.direction_index = 0

        self.image = self.player_walk[self.direction_index][self.frame_index]
        self.image = pygame.transform.scale_by(self.image, 4)
        self.x = config.SCREEN_WIDTH/2
        self.y = config.SCREEN_HEIGHT/2
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.player_speed = 3
    #
    # Player input listener
    #
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.player_speed
            print(self.x, ',', self.y)
            self.direction_index = 2
            self.animation_state()
        elif keys[pygame.K_d]:
            self.x += self.player_speed
            print(self.x, ',', self.y)
            self.direction_index = 1
            self.animation_state()
        elif keys[pygame.K_s]:
            self.y += self.player_speed
            print(self.x, ',', self.y)
            self.direction_index = 0
            self.animation_state()
        elif keys[pygame.K_a]:
            self.x -= self.player_speed
            print(self.x, ',', self.y)
            self.direction_index = 3
            self.animation_state()
    
    #
    # This method updates the animation frame by incrementing the frame index
    #
    def animation_state(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.player_walk[self.direction_index]):
            self.frame_index = 0

    #
    # This method updates the player information
    #
    def update(self):
        self.player_input()
        self.image = self.player_walk[self.direction_index][int(self.frame_index)]
        self.image = pygame.transform.scale_by(self.image, 4)