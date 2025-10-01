def count_vowels(str):
    kounter = 0
    new_str = str.lower()
    for i in new_str:
        match i:
            case 'a':
                kounter += 1
            case 'e':
                kounter += 1
            case 'i':
                kounter += 1
            case 'o':
                kounter += 1
            case 'u':
                kounter += 1
            case 'y':
                kounter += 1
    return f"Гласных букв: ", kounter

print(count_vowels(input("Введите строку: ")))