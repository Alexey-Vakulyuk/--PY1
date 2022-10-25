def delete(list_, index=None):
    if index is None:   # если пользователь не переопределил значение по умолчанию
        index = -1
    if index != -1:   # слайсирование для непоследнего индекса
        first_part = list_[:index]
        second_part = list_[1+index:]
        return first_part + second_part
    else:   # слайсирование для последнего индекса
        return list_[:index]


print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
