import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str) -> list[dict]:
    with open(filename) as f:  # открытие конвертируемого файла
        headers = f.readline().split('\n')[0].split(',')  # выделение заголовков из файла
        dataset = []  # список строк значений
        for value in f.readlines():
            dataset.append(value.split('\n')[0].split(','))  # удаление разделителей значений и строк

        dict_list = []  # список словарей
        for data_list in dataset:   # для каждой строки в dataset
            d = {}  # словарь заголовок: значение
            for j, header in enumerate(headers):
                d[header] = data_list[j]
            dict_list.append(d)

        return dict_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
