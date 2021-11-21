# 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
# YAML-формата. Для этого: Подготовить данные для записи в виде словаря, в котором первому ключу соответствует
# список, второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с
# юникод-символом, отсутствующим в кодировке ASCII (например, €); Реализовать сохранение данных в файл формата YAML —
# например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True; Реализовать считывание данных из созданного
# файла и проверить, совпадают ли они с исходными

import yaml

data = {
    "1": ["first", "second", "third"],
    "2": 2,
    "3": {
        "1": "100€",
        "2": "200€",
        "3": "300€"
    }
}


def write_to_yaml(some_dict):
    with open('file.yaml', "w", encoding="utf-8") as f_n_w:
        yaml.dump(data, f_n_w, default_flow_style=False, allow_unicode=True, sort_keys=False)


write_to_yaml(data)

with open('file.yaml', "r", encoding="utf-8") as f_n_r:
    if data == yaml.load(f_n_r, Loader=yaml.SafeLoader):
        print("The data is the same.")
    else:
        print("The data is not the same, somethings wrong.")
