list_numbers = []

n = int(input("Введите количество чисел: "))

for i in range(1, n+1):
    j = int(input("Введите число: "))
    list_numbers.append(j)

print(f"Ввод списка завершён: {list_numbers}")

total = 0
k = 0
for i in list_numbers:
    total += i
    print(f"Промежуточное значение суммы: {total}")
    k += 1
    print(f"Промежуточное значение счётчика {k}")

sr = total / k
print(f"Средне округлённое: {sr}")