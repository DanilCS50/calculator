import logging  #Импорт модулей
import basic        
import advancexd

logging.basicConfig(                    #Добавление параметров логирования
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

logger.info("Программа началась")
operation = input("Введите операцию без пробелов(+; -; *: /; **; f)") #Запрос операции у пользователя
logger.debug("Пользователь ввёл операцию: %s", operation)
if operation == 'f':        #Проверка операции на 2 ситуации (факториал или нет)
    f = int(input(f"Введите число: "))
    logger.debug("Пользователь ввёл число для факториала: %s", f)
else:
    a = int(input("Введите первое число (над ним будут происходть все операции): "))
    b = int(input("Введите второе число: "))
    logger.debug("Пользователь ввёл две переменных %s, %s", a, b)


match operation:        #Подбираем операция
    case '+':
        logger.debug("Пользователь запросил операцию сложения %s, %s", a, b)
        print(basic.addition(a, b))
    case '-':
        logger.debug("Пользователь запросил операцию вычитания %s, %s", a, b)
        print(basic.subtraction(a, b))
    case '*':
        logger.debug("Пользователь запросил операцию умножения %s, %s", a, b)
        print(basic.multiplication(a, b))
    case '/':
        logger.debug("Пользователь запросил операцию деления %s, %s", a, b)
        print(basic.division(a, b))
    case '**':
        logger.debug("Пользователь запросил операцию возведения в степень %s, %s", a, b)
        print(advancexd.degree(f))
    case 'f':
        logger.debug("Пользователь запросил операцию факториал %s, %s", f)
        print(advancexd.factorial(f))
    case _:
        logger.warning("Команда не распознана: %s", operation) #Ошибка. Операция не распознана