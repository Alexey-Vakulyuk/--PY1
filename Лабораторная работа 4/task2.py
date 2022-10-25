def get_count_char(str_):  # функция, возвращающая словарь с частотой каждого символа
    str_ = str_.lower()  # приведение строки к единому регистру
    unique_chars = set(str_)  # множество уникальных символов
    letters = []
    for char in unique_chars:  # цикл для поиска использованных в строке букв
        if char.isalpha():
            letters.append(char)
    d = {}
    DEFAULT_COUNT = 0
    for letter in str_:  # цикл для подсчета количества каждой буквы в строке
        if letter in letters:
            d[letter] = d.get(letter, DEFAULT_COUNT) + 1
    return d


def get_percentage(d):  # функция, возвращающая новый словарь, где количество каждого элемента заменено на процентное
    # отношение ко всем символам
    PERCENT = 100
    sum_value = sum(d.values())  # суммарное количество букв
    for letter in d:
        d[letter] /= sum_value / PERCENT   # высчитывание процента
    return d


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_percentage(get_count_char(main_str)))
