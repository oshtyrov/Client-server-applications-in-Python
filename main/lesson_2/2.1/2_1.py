# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
# файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
# данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
# os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
# поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
# «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
# каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import glob
import os
import csv
import re


def get_data():
    def get_substring(string):  # функция поиска подстроки на основе регулярного выражения
        return regexp.search(string).group(1)

    os.chdir("./")
    fls_lst = [file for file in glob.glob("*.txt")]  # находим все тхт файлы в директории скрипта
    regexp = re.compile(":+\s+(.*)$")  # регулярное выражение для поиска подстроки, согласно условию задания
    headers = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
    os_prod_list = []  # зачем создавать эти списки согласно условию задания, остается неясным
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in fls_lst:
        with open(file) as f_n:
            f_n_reader = csv.reader(f_n)
            for row in f_n_reader:
                row = row[0]
                if headers[0] in row:  # "Изготовитель системы"
                    os_prod_list.append(get_substring(row))
                if headers[1] in row:  # "Название ОС"
                    os_name_list.append(get_substring(row))
                if headers[2] in row:  # "Код продукта"
                    os_code_list.append(get_substring(row))
                if headers[3] in row:  # "Тип системы"
                    os_type_list.append(get_substring(row))
    main_data = [headers]
    atr_lists = [os_prod_list, os_name_list, os_code_list, os_type_list]
    for i in range(len(atr_lists[0])):
        product = [el[i] for el in atr_lists]
        main_data.append(product)
    return main_data


def write_to_csv(file):
    data = get_data()
    with open(file, 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        f_n_writer.writerows(data)


write_to_csv("test.csv")

print(get_data())
