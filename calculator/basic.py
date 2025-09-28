import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def addition(a, b):

    """Функция сложения. Принимате два чила типа int и сладывате их. 
    Возвращает одно число типа int."""

    logger.info("Запущена функция сложения")
    result = a + b
    logger.debug("Результат сложения: %s", result)
    logger.info("Результат возвращается")
    return result

def subtraction(a, b):

    """Операция вычитания. Принимает два числа типа int и вычитает второе число из первого. 
    Возвращае одно число типа int."""

    logger.info("Запущена функция вычитания")
    result = a - b
    logger.debug("Результат вычитания: %s", result)
    logger.info("Результат возвращается")
    return result

def multiplication(a, b):

    """Операция умножения. Принимает два числа типа int и перемножает.
    Возвращает одно число типа int"""

    logger.info("Запущена функция умножения")
    result = a * b
    logger.debug("Результат умножения: %s", result)
    logger.info("Результат возвращается")
    return result

def division(a, b):
    
    """Операция деления. Принимает два числа типа int и делит первое число на второе.
    Возвращает одно число типа int"""
    
    logger.info("Запущена функция деления")
    result = a / b
    logger.debug("Результат деления: %s", result)
    logger.info("Результат возвращается")
    return result

