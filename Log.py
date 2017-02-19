''' Fast logging by KDV '''

import logging 
import handler

logger = logging.getLogger('Denis')

logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG  )

logging.debug('Debug') 
logging.info('Информационное сообщение ')
logging.error('Ошибка')
logging.warning('Предупреждение') 
logging.critical( 'БЕГИ!!!!!!!' )