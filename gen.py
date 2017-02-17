''' Fast genetators by Phonphey '''

#!/usr/bin/env python3

#- * -coding: utf - 8 - * -

import random
import numpy as np

COLL_OBS = ["*", "-", "_", "A",
            "B", "C"]  # Коллекция припятствий


class Gen():
    ''' Класс генераторов'''

    def rand_map_gen(self):
        ''' Функция-генератор случайной, временной карты '''
        gen_map = list()
        unluky_obs = 0
        for i in range(0, 100, 1):  # Генератор карты
            tmp_str = ""
            tumb = True
            k = 0
            while tumb:  # Генератор строки в карте

                if k == 0:  # Проверяем нужна ли стенка
                    tmp_str += "| "

                tmp_unluky_obs = unluky_obs
                # Вероятность появления препятствия
                unluky_obs = random.randint(1, 45)
                # Выбор случайного препятствия
                rand_obs = random.choice(COLL_OBS)

                # Проверка вероятности и контроль длинны строки
                if unluky_obs > 17 and tmp_unluky_obs < 17 and len(tmp_str + rand_obs) <= 12:
                    tmp_str += random.choice(COLL_OBS)

                elif len(tmp_str + rand_obs) <= 12:
                    tmp_str += " "

                elif len(tmp_str + rand_obs) >= 12:
                    tmp_str = tmp_str[:10]
                    tumb = False
                    tmp_str += " |"

                k += 1

            gen_map.append(tmp_str)
        return gen_map

if __name__ == "__main__":
    TMP_CLASS = Gen()
    TMP = TMP_CLASS.rand_map_gen()
    print(TMP, len(TMP[0]), len(TMP[55]))
