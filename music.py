import log # Импорт Логгера

try:

    import sound_const # Импортируем библиотеку с аудио файлами
    import random
    import log # Импорт Логгера
    import simpleaudio as sa
    import os

except ImportError:

    log.logging.critical('Ошибка импорта')

else:
    log.logging.info('Импорт прошел успешно')

class Mus(): # Создаем класс , содержащий функции

    def rand_mus_gen(self): # Функция ,держащая цикл создающий список с 10 случайными числами от 1 до 10
        seed = os.urandom(10) # Выделяем 10 байт мусора
        random.seed(seed) # Закладываем семя генерации
        gen_mus = list() # Сам список
        tumb = True
        while tumb: # Функция
            tmp = random.randint(1, 10)
            gen_mus.append(tmp)
            if len(gen_mus) > 10: # Задаем условие при котором цикл заканчивается
                tumb = False


        return gen_mus

    log.logging.info('Список случайных чисел был создан')

    def build_mus(self, gen_mus): # Функция ,содержащая список, в котором каждому значению присвАивается в цикле звук
        bld_mus = list()
        for i in range(0,  len(gen_mus) - 1, 1):      # Цикл
            if gen_mus[i] == 1:                       # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND1      #   
            elif gen_mus[i] == 2:                     # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND2      # 
            elif gen_mus[i] == 3:                     # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND3      #
            elif gen_mus[i] == 4:                     # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND4      #
            elif gen_mus[i] == 5:                     # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND5      #
            elif gen_mus[i] == 6:                     # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND6      #
            elif gen_mus[i] == 7:                     # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND7      #
            elif gen_mus[i] == 8:                     # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND8      #
            elif gen_mus[i] == 9:                     # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND9      #
            elif gen_mus[i] == 10:                    # Условие прикотором значению из списка присваевается звук
                 bld_mus[i] = sound_const.SOUND10     #

    log.logging.info('Каждому значению из списка был присвоен звук')
    log.logging.info('ПЕРЕХОД К МОДУЛЮ ГЕНЕРАЦИИ КАРТЫ')
if __name__ == "__main__":
    TMP_CLASS = Mus()
    print(TMP_CLASS.rand_mus_gen())

