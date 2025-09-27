def max_in_list(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            print(f"Сравниваются {n} и {max_num}")
            max_num = n
            print(f"Максимальное число {max_num}")
    return max_num

nums = [-5, -10, -3]
print("Максимум:", max_in_list(nums))
