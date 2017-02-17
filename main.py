#!/usr/bin/env python3

#- * -coding: ascii- * -

# Импортируем библиотеку pygame

import pygame
from pygame import *
import gen
import header
import player


def main():
    ''' Основная временная функция '''

    pygame.init()  # Инициализация PyGame, обязательная строчка
    screen = pygame.display.set_mode(header.DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Ritualist")  # Пишем в шапку

    # Создание видимой поверхности# будем использовать как фон
    bg = pygame.Surface(header.DISPLAY)
    # Заливаем поверхность сплошным цветом
    bg.fill(pygame.Color(header.BACKGROUND_COLOR))

    # Создание экземпляра класса генераторов
    _gen = gen.Gen()
    # Создаём карту
    _map = _gen.rand_map_gen()

    left = right = False    # по умолчанию — стоим

    hero = player.player(30, 30)  # создаем героя по (x,y) координатам

    timer = pygame.time.Clock()  # Создание  таймера

    while 1:  # Основной цикл программы
        timer.tick(60)
        x = y = 0
        
        for i in pygame.event.get():
            # Обрабатываем события
            if i.type == QUIT:
                raise SystemExit("QUIT")
            if i.type == KEYDOWN and i.key == K_LEFT:
                left = True
            if i.type == KEYDOWN and i.key == K_RIGHT:
                right = True

            if i.type == KEYUP and i.key == K_RIGHT:
                right = False
            if i.type == KEYUP and i.key == K_LEFT:
                left = False

        # Каждую итерацию необходимо всё перерисовывать
        screen.blit(bg, (0, 0))
        # Обновление и вывод всех изменений на экран

        for row in _map:  # вся строка
            for col in row:  # каждый символ
                if col == "|":
                    # создаем блок, заливаем его цветом и рисеум его
                    pf = pygame.Surface(header.PLATFORM)
                    pf.fill(pygame.Color(header.PLATFORM_COLOR))
                    screen.blit(pf, (x, y))

                # Блоки платформы ставятся на ширине блоков
                x += header.PLATFORM_WIDTH
            # То же самое и с высотой
            y += header.PLATFORM_HEIGHT
            # На каждой новой строчке начинаем с нуля
            x = 0

        hero.draw(screen)  # отображение

        hero.update(left, right)  # передвижение

        pygame.display.update()
if __name__ == "__main__":
    main()
