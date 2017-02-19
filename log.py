''' Fast logging by KDV '''

import logging # импорт библиотеки logging

logger = logging.getLogger('Denis') # ввод ненужной переменной 

logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG) # казываем формат выводимой строки


