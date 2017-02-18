''' Fast genetators by Phonphey '''

#!/usr/bin/env python3

#- * -coding: utf - 8 - * -

import random
import header


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
                    tmp_str += "|"

                old_lucky = lucky
                # Вероятность появления препятствия
                lucky = random.randint(1, 100)

                if lucky <= 50 and old_lucky > 50:  # Проверка вероятности
                    tmp_str += random.choice(header.COLL_OBS)

                else:
                    tmp_str += " "

                if len(tmp_str) >= 12:
                    tmp_str = tmp_str[:11]
                    tmp_str += "|"
                    tumb = False

                i += 1

            gen_map.append(tmp_str)

        return gen_map

if __name__ == "__main__":
    TMP_CLASS = Gen()
    print(TMP_CLASS.rand_map_gen())
