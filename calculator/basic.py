import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def addition(x, y):
    logger.info("Запущена функция сложения")
    z = x + y
    logger.debug("Результат сложения: %s", z)
    logger.info("Результат возвращается")
    return z

def subtraction(x, y):
    logger.info("Запущена функция вычитания")
    z = x - y
    logger.debug("Результат вычитания: %s", z)
    logger.info("Результат возвращается")
    return z

def multiplication(x, y):
    logger.info("Запущена функция умножения")
    z = x * y
    logger.debug("Результат умножения: %s", z)
    logger.info("Результат возвращается")
    return z

def division(x, y):
    logger.info("Запущена функция деления")
    z = x / y
    logger.debug("Результат деления: %s", z)
    logger.info("Результат возвращается")
    return z

