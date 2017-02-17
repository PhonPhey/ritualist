''' Platform and other class '''

import header
import pygame

class Platform(pygame.sprite.Sprite):
    ''' Platform class '''

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(header.PLATFORM)
        self.image.fill(pygame.Color(header.PLATFORM_COLOR))
        self.rect = pygame.Rect(x, y, header.PLATFORM_WIDTH, header.PLATFORM_HEIGHT)