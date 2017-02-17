import pygame
import header

class player(pygame.sprite.Sprite):
    '''Player class'''

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = pygame.Surface(header.SPRITE)
        self.image.fill(pygame.Color(header.COLOR))
        self.rect = pygame.Rect(x, y, header.WIDTH, header.HEIGHT) # прямоугольный объект

    def update(self, left, right):
        ''' Update window method '''

        if left:
            self.xvel = -header.MOVE_SPEED # Лево = x- n

        if right:
            self.xvel = header.MOVE_SPEED # Право = x + n

        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0

        self.rect.x += self.xvel # переносим свои положение на xvel

    def draw(self, screen): # Выводим себя на экран
        ''' Draw sprite method '''

        screen.blit(self.image, (self.rect.x, self.rect.y))