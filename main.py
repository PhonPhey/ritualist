''' Main module of Ritualist '''

#!/usr/bin/python3

#- * -coding: utf-8- * -
import log


try:
    import music
    import arcade  # Ипортируем библиотеку arcade(построенную на pyglet)
    import gen  # Импорт генератора карты
    import base_const  # Импорт заголовочного файла
    import log # Импорт Логгера
    import text_sprite_const as tsc

except ImportError:

    log.logging.critical('Ошибка импорта')

else:
    log.logging.info('Импорт прошел успешно')

def main():
    ''' Main function '''
    # Открываем окно с задаными параметрами высоты, ширины и заголовка
    arcade.open_window(base_const.WIN_TITLE, base_const.WIN_WIDTH,
                       base_const.WIN_HEIGHT)

    arcade.set_background_color(
        base_const.WIN_BACKGROUND_COLOR)  # Задаём цвет фона окна

    _gen = gen.Gen()  # Создаём экземпляр класса генераторов

    log.logging.info('Цвет фона задан')
    log.logging.info('Экземпляр класса генераторов создан')

    arcade.start_render()  # Начинаем рендер в открытом окне

    log.logging.info('Начат рендер в открытом окне ')

    _gen.build_map(_gen.rand_map_gen())  # генерируем ,cтроим и рисуем карту
    tsc.ALL_SPRITES[1].draw()

    log.logging.info('Генерация и прорисовка карты')

    arcade.finish_render()  # Заканчиваем рендер в открытом окне

    log.logging.info('Рендер закончен успешно')

    log.logging.info('Приложение запущено успешно')

    arcade.run()  # Запускаем приложение



if __name__ == "__main__":
    main()  # Инициализируем основную функцию
 