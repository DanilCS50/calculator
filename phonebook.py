def add_number(numbers):
    person = input("Введите имя контакта: ")
    if person in numbers:
        new_number = input("Контакт найден. Введите номер: ")
        numbers[person].append(new_number)
    else:
        print("Контакт не найден.")
    print(numbers)


def delete_number(numbers):
    person = input("Введите имя контакта которого хотите удалить: ")
    if person in numbers:
        del numbers[person]
    else:
        print("Контакт не найден")
    print(numbers)
    

def print_number(numbers):
    person = input("Введите имя контакта: ")
    if person in numbers:
        print(f"Контакт найден: {numbers[person]}") 
    else:
        print("Контакт не найден")



phonebook = {
    "Vlad":  ["+7 903 450 50 40"],
    "Zakhar": ["+7 807 573 38 41"],
    "Danil": ["+7 952 953 59 39"]
}

add_number(phonebook)
delete_number(phonebook)
print_number(phonebook)
