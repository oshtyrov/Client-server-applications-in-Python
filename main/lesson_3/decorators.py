"""Декораторы"""

import sys
import logging
import logs.client_log_config
import logs.server_log_config
import traceback
import inspect

# метод определения модуля, источника запуска.
# if "client" in sys.argv[0]:
if sys.argv[0].find('client') == -1:
    print(sys.argv[0])
    # если не клиент то сервер!
    LOGGER = logging.getLogger('server')
else:
    # если не сервер, то клиент
    print(sys.argv[0])
    LOGGER = logging.getLogger('client')


def log(func_to_log):
    """Функция-декоратор"""
    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}.'
                     f'Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}.'
                     f'Вызов из функции {inspect.stack()[1][3]}')
        return ret
    return log_saver
