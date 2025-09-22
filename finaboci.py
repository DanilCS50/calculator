fin = [0, 1]

x = 0
y = 1

n = int(input("Укажите количество чисел finaboci: "))
print(f"Числа финабочи: {fin[0], fin[1]}, ", end='')
for i in range(1, n+1):
    next_fin_number = (fin[x]) + (fin[y])
    fin.append(next_fin_number)
    print(next_fin_number, end=', ')
    x += 1
    y += 1
