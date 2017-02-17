#!/usr/bin/env python3

#- * -coding: ascii- * -

# Импортируем библиотеку pygame

import pygame
from pygame import *
import gen
import header
import player
import pl_obs as plat


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

    entities = pygame.sprite.Group() # Все объекты
    platforms = list() # то, во что мы будем врезаться или опираться
    entities.add(hero)

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
                    pf = plat.Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)

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
