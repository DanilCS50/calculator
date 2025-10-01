import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def factorial(f):

    """Операция факториал. Принимает одно число типа int и вычисляет факториал этого числа
    с помощью рекурсии. Возвращает одно число типа int"""

    logger.info("Функция факториала запущена")
    if f == 1 or f == 0:
        logger.debug("Возвращение функции x == 1")
        return f
    else:
        logger.debug("Рекурсия: x = %s", f)
        return f * factorial(f-1)
        
def degree(a, b):

    """Операция возведения в степень. Принимает два числа типа int и 
    возводит первое число в степень второго числа. Возвращает одно число типа int"""

    logger.info("Функция возведения в степень запущена")
    result = a ** b
    logger.debug("Результат возведении в стпень = %s", result)
    logger.info("Функция возвращает значение")
    return result