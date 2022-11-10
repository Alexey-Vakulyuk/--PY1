import string
from random import sample


def get_random_password(n: int = 8) -> str:

    ABC = string.ascii_uppercase + string.ascii_lowercase + string.digits   # Алфавит символов для генерации пароля
    password = ''.join(sample(ABC, n))  # Генерация списка длины n случайных символов из ABC и объединение его
    # элементов в одну строку

    return password


print(get_random_password())
