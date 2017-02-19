''' Fast logging by KDV '''

import logging  # импорт библиотеки logging

LOGGER = logging.getLogger('Denis')  # ввод ненужной переменной

# казываем формат выводимой строки
logging.basicConfig(
    format='%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG)
