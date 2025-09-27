import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def factorial(x):
    logger.info("Функция факториала запущена")
    if x == 1:
        logger.debug("Возвращение функции x == 1")
        return x
    else:
        logger.debug("Рекурсия: x = %s", x)
        return x * factorial(x-1)
        

def degree(x, y):
    logger.info("Функция возведения в стпень запущена")
    z = x ** y
    logger.debug("Результат возведении в стпень = %s", z)
    logger.info("Функция возвращает значение")
    return zimport logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def factorial(x):
    logger.info("Функция факториала запущена")
    if x == 1:
        logger.debug("Возвращение функции x == 1")
        return x
    else:
        logger.debug("Рекурсия: x = %s", x)
        return x * factorial(x-1)
        

def degree(x, y):
    logger.info("Функция возведения в стпень запущена")
    z = x ** y
    logger.debug("Результат возведении в стпень = %s", z)
    logger.info("Функция возвращает значение")
    return z