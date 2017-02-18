#!/usr/bin/python3

#- * -coding: utf-8- * -

import pyglet  # Импорт pyglet
import arcade  # Ипортируем библиотеку arcade(построенную на pyglet)

import gen  # Импорт генератора карты
import header  # Импорт заголовочного файла


def main():
    ''' Main function '''
    arcade.open_window(header.WIN_TITLE, header.WIN_HEIGHT,
                       header.WIN_WIDTH)  # Открываем окно с задаными параметрами высоты, ширины и заголовка

    arcade.set_background_color(
        header.WIN_BACKGROUND_COLOR)  # Задаём цвет фона окна

    arcade.start_render()  # Начинаем рендер в открытом окне

    arcade.finish_render()  # Заканчиваем рендер в открытом окне

    arcade.run()  # Запускаем приложение

if __name__ == "__main__":
    main()  # Инициализируем основную функцию
