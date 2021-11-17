# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.
a = '\n'

data_str = ['разработка', 'сокет', 'декоратор']
data_unicode_str = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
                    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
for el in data_unicode_str + data_str:
    print(el, type(el))
print(a)

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

for el in ['class', 'function', 'method']:
    code = f"b'{el}'"
    code = eval(code)
    print(code, type(code), len(code))
print(a)

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

for el in ['attribute', 'класс', 'функция', 'type']:
    try:
        code = f"b'{el}'"
        code = eval(code)
    except SyntaxError:
        print(f'"{el}" cannot be written in bytes type!')
    else:
        print(f'"{el}" written in bytes type successfully.')
print(a)

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

words_4_bytes = [el.encode("utf-8") for el in ["разработка", "администрирование", "protocol", "standard"]]
print(words_4_bytes)
words_4_str = [el.decode("utf-8") for el in words_4_bytes]
print(words_4_str)
print(a)

# 5. Выполнить пинг веб-ресурсов google.com, youtube.com и преобразовать результаты из байтовового в строковый тип на
# кириллице.

import subprocess
import chardet


def get_ping(website):
    ping = subprocess.Popen(["ping", website], stdout=subprocess.PIPE)
    for el in ping.stdout:
        result = chardet.detect(el)
        el = el.decode(result['encoding']).encode('utf-8')
        print(el.decode('utf-8'))


websites = ['google.com', 'youtube.com']
for web in websites:
    get_ping(web)

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести
# его содержимое.

with open('test_file.txt', "rb") as f_n:
    data = f_n.read()
    enc = chardet.detect(data)
    data = data.decode(enc['encoding']).encode('utf-8').decode('utf-8 ')
    print(data)


