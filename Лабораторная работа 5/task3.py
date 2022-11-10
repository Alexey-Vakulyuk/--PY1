from random import randint


def get_unique_list_numbers() -> list[int]:
    LIST_LEN = 15   # Размер списка 15 чисел
    LEFT_BORDER = -10   # Левая граница списка
    RIGHT_BORDER = 10   # Правая граница списка
    random_list = []    # Создание списка для случайных чисел

    while len(random_list) <= LIST_LEN:
        random_number = randint(LEFT_BORDER, RIGHT_BORDER)    # Случайное целое число от -10 до 10 включительно
        if random_number not in random_list:    # Если число еще не было в списке добавляем его
            random_list.append(random_number)

    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
