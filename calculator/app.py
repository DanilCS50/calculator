import calculator.basic as basic
import calculator.advancexd as advancexd

recognition = input("Введите функцию без пробелов(+; -; *: /; **; f)")
if recognition == 'f':
    z = int(input("Введите число: "))
else:
    x = int(input("Введите 1 число (оно бедет вычитаемым, делимым и т.д.)"))
    y = int(input("Введите 1 число (оно бедет вычитаемым, делимым и т.д.)"))

if recognition == '+':
    print(basic.addition(x, y))
elif recognition == '-':
    print(basic.subtraction(x, y))
elif recognition == '*':
    print(basic.multiplication(x, y))
elif recognition == '/':
    print(basic.division(x, y))
elif recognition == '**':
    print(advancexd.degree(x, y))
elif recognition == 'f':
    print(advancexd.factorial(z))
else:
    print("Команда не распознана!")