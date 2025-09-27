import logging
import basic
import advancexd

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

logger.info("Программа началась")
recognition = input("Введите операцию без пробелов(+; -; *: /; **; f)")
logger.debug("Пользователь ввёл операцию: %s", recognition)
if recognition == 'f':
    z = int(input(f"Введите число: "))
    logger.debug("Пользователь ввёл число для факториала: %s", z)
else:
    x = int(input("Введите 1 число (оно будет вычитаемым и т.п.)"))
    y = int(input("Введите 2 число (оно будет делимым и т.п.)"))
    logger.debug("Пользователь ввёл две переменных %s, %s", x, y)

if recognition == '+':
    logger.debug("Пользователь запросил операцию сложения %s, %s", x, y)
    print(basic.addition(x, y))
elif recognition == '-':
    logger.debug("Пользователь запросил операцию вычитания %s, %s", x, y)
    print(basic.subtraction(x, y))
elif recognition == '*':
    logger.debug("Пользователь запросил операцию умножения %s, %s", x, y)
    print(basic.multiplication(x, y))
elif recognition == '/':
    logger.debug("Пользователь запросил операцию деления %s, %s", x, y)
    print(basic.division(x, y))
elif recognition == '**':
    logger.debug("Пользователь запросил операцию возведения в стпень %s, %s", x, y)
    print(advancexd.degree(x, y))
elif recognition == 'f':
    logger.debug("Пользователь запросил операцию факториал %s", z)
    print(advancexd.factorial(z))
else:
    logger.warning("Команда не распознана: %s", recognition)
    import logging
import basic
import advancexd

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

logger.info("Программа началась")
recognition = input("Введите операцию без пробелов(+; -; *: /; **; f)")
logger.debug("Пользователь ввёл операцию: %s", recognition)
if recognition == 'f':
    z = int(input(f"Введите число: "))
    logger.debug("Пользователь ввёл число для факториала: %s", z)
else:
    x = int(input("Введите 1 число (оно будет вычитаемым и т.п.)"))
    y = int(input("Введите 2 число (оно будет делимым и т.п.)"))
    logger.debug("Пользователь ввёл две переменных %s, %s", x, y)

if recognition == '+':
    logger.debug("Пользователь запросил операцию сложения %s, %s", x, y)
    print(basic.addition(x, y))
elif recognition == '-':
    logger.debug("Пользователь запросил операцию вычитания %s, %s", x, y)
    print(basic.subtraction(x, y))
elif recognition == '*':
    logger.debug("Пользователь запросил операцию умножения %s, %s", x, y)
    print(basic.multiplication(x, y))
elif recognition == '/':
    logger.debug("Пользователь запросил операцию деления %s, %s", x, y)
    print(basic.division(x, y))
elif recognition == '**':
    logger.debug("Пользователь запросил операцию возведения в стпень %s, %s", x, y)
    print(advancexd.degree(x, y))
elif recognition == 'f':
    logger.debug("Пользователь запросил операцию факториал %s", z)
    print(advancexd.factorial(z))
else:
    logger.warning("Команда не распознана: %s", recognition)
    