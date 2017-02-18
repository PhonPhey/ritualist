#!/usr/bin/python3

#- * -coding: utf-8- * -

import arcade  # Ипортируем библиотеку arcade(построенную на pyglet)

import gen  # Импорт генератора карты
import base_const  # Импорт заголовочного файла


def main():
    ''' Main function '''
    # Открываем окно с задаными параметрами высоты, ширины и заголовка
    arcade.open_window(base_const.WIN_TITLE, base_const.WIN_WIDTH,
                       base_const.WIN_HEIGHT)

    arcade.set_background_color(
        base_const.WIN_BACKGROUND_COLOR)  # Задаём цвет фона окна

    _gen = gen.Gen()  # Создаём экземпляр класса генераторов

    arcade.start_render()  # Начинаем рендер в открытом окне

    _gen.build_map(_gen.rand_map_gen())  # генерируем ,cтроим и рисуем карту

    arcade.finish_render()  # Заканчиваем рендер в открытом окне

    arcade.run()  # Запускаем приложение

if __name__ == "__main__":
    main()  # Инициализируем основную функцию
