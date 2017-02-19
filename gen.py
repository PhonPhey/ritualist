''' Fast genetators by Phonphey '''

#!/usr/bin/env python3

#- * -coding: utf - 8 - * -
import log

try:
    import random
    import base_const
    import text_sprite_const
    import arcade
    import log
    
except ImportError:
    
    log.logging.critical('Ошибка импорта')

else: 
    log.logging.info('Импорт прошел успешно')

class Gen():
    ''' Класс генераторов'''

    def rand_map_gen(self):
        ''' Генератор временной карты '''

        gen_map = list()  # ПЕРЕМЕННАЯ СОДЕРЖАЩАЯ КАРТУ

        for _ in range(0, 150, 1):  # Цикл генерации карты

            # Вероятность появления препятствия
            lucky = random.randint(1, 100)
            i = 0  # Номер символа в строке
            tumb = True  # Тумблер
            tmp_str = ""  # Временная строка

            while tumb:  # Цикл генерации строки

                if i == 0:  # Проверка на надобность стенки
                    tmp_str += "\\"

                old_lucky = lucky
                # Вероятность появления препятствия
                lucky = random.randint(1, 100)

                if lucky <= 50 and old_lucky > 50:  # Проверка вероятности
                    tmp_str += random.choice(base_const.COLL_OBS)

                else:
                    tmp_str += " "

                if len(tmp_str) >= 12:
                    tmp_str = tmp_str[:11]
                    tmp_str += "/"
                    tumb = False

                i += 1

            gen_map.append(tmp_str)

        return gen_map
        log.logging.info('Карта создана') 

    def build_map(self, gen_map):
        ''' Build map on text map '''
        x_coor = 16
        y_coor = 0
        for row in gen_map:  # вся строка
            for col in row:  # каждый символ
                if col == "\\":
                    wall = arcade.arcade.load_texture(
                        text_sprite_const.STONE_WALL)  # Загружаем текстуру

                    # Рисаем стены с текстурой, которую загрузили ранее
                    arcade.draw_texture_rectangle(
                        x_coor, y_coor, base_const.WIN_WIDTH * base_const.TEXTURE_WALL_WIDTH_SCALE,
                        base_const.WIN_HEIGHT * base_const.TEXTURE_WALL_HEIGHT_SCALE, wall, 180)
                
                elif col == "/":
                    wall = arcade.load_texture(
                        text_sprite_const.STONE_WALL)  # Загружаем текстуру
              
                    # Рисаем стены с текстурой, которую загрузили ранее
                    arcade.draw_texture_rectangle(
                        x_coor, y_coor, base_const.WIN_WIDTH * base_const.TEXTURE_WALL_WIDTH_SCALE,
                        base_const.WIN_HEIGHT * base_const.TEXTURE_WALL_HEIGHT_SCALE, wall)

                elif col == " ":
                    floor = arcade.load_texture(
                        text_sprite_const.STONE_FLOOR)  # Загружаем текстуру

                    arcade.draw_texture_rectangle(
                        x_coor, y_coor, base_const.WIN_WIDTH * base_const.TEXTURE_FLOOR_WIDTH_SCALE,
                        base_const.WIN_HEIGHT * base_const.TEXTURE_FLOOR_HEIGHT_SCALE, floor)

                x_coor += base_const.PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y_coor += base_const.PLATFORM_HEIGHT  # то же самое и с высотой
            x_coor = 16  # на каждой новой строчке начинаем с нуля

    log.logging.info('Загрузка текстуры')

    log.logging.info('Прорисовка карты с текстурами')

    log.logging.info('Карта готова')

    log.logging.info('ПЕРЕХОД К ОСНОВНОМУ МОДУЛЮ')


if __name__ == "__main__":
    TMP_CLASS = Gen()
    print(TMP_CLASS.rand_map_gen())
