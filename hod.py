def compare(a, b):
    if a > b:
        return b
    elif b > a:
        return a

a = int(input("Введите число: "))
b = int(input("Введите второе число: "))

if a > b:
    x = a % b
elif b > a:
    x = b % a
else:
    x = 0

for i in range(1,):
    if x == 0:
        print("Нaибольший нод: ", compare(a, b))
        break

    if i == 1:
        less = x
        bigger = compare(a, b)
    tp = less
    less = bigger % less

    if less == 0:
        print("Наибольший НОД: ", less)
        break
    else:
        bigger = tp
    
