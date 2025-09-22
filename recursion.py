def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
        

a = int(input("Введите число: "))
print(f"Факториал: {factorial(a)}")