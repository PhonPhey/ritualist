#!/usr/bin/python3

#- * -coding: utf-8- * -

import arcade  # Ипортируем библиотеку arcade(построенную на pyglet)

import gen  # Импорт генератора карты
import header  # Импорт заголовочного файла


def main():
    ''' Main function '''
    # Открываем окно с задаными параметрами высоты, ширины и заголовка
    arcade.open_window(header.WIN_TITLE, header.WIN_WIDTH,
                       header.WIN_HEIGHT)

    arcade.set_background_color(
        header.WIN_BACKGROUND_COLOR)  # Задаём цвет фона окна

    _gen = gen.Gen()  # Создаём экземпляр класса генераторов
    _map = _gen.rand_map_gen()  # Генерируем карту

    arcade.start_render()  # Начинаем рендер в открытом окне

    _gen.build_map(_map)  # Строим и рисуем карту

    arcade.finish_render()  # Заканчиваем рендер в открытом окне

    arcade.run()  # Запускаем приложение

if __name__ == "__main__":
    main()  # Инициализируем основную функцию
