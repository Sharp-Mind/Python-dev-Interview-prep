"""
5. Усовершенствовать первую функцию из предыдущего примера.

Необходимо во втором списке часть строковых значений заменить на значения типа example345
(строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных).

Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.

Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""

import os
import string
from random import randint, choice, shuffle


letters = string.ascii_letters

list_a = [f'{choice(letters)}{choice(letters)}' for _ in range(5)]
list_a_half_2 = [
    f'{choice(letters)}{choice(letters)}{randint(1, 100)}' for _ in range(5)]
list_a.extend(list_a_half_2)
shuffle(list_a)

list_b = [randint(1, 100) for _ in range(10)]
zipped_list = list(zip(list_a, list_b))

# полный путь до файла:
path = "/home/redlance/test.txt"


def find_it(lookfor, repl=None):
    found_list = []   # список для вывода перечисления найденных строк
    new_data = []     # список для перезаписи файла после изменения

    with open(path, 'r') as f:
        data = f.readlines()

    found = False  # для вывода сообщения о первом вхождении
    for line in data:

        if lookfor in line and found == False:
            print(f'\nОбъект "{lookfor}" найден первым в "{line}"\n')
            found = True
            found_list.append(line)
            if repl != None:
                new_data.append(line.replace(
                    line[line.find(lookfor)], repl))

        elif lookfor in line and found == True:
            found_list.append(line)
            if repl != None:
                new_data.append(line.replace(
                    line[line.find(lookfor)], repl))
        elif repl != None and lookfor not in line:
            new_data.append(line)

    if len(found_list) > 0:
        print(f'Объект "{lookfor}" найден в строках:')
        for i in found_list:
            print(i, end='')
        print('\n' + '----------' + '\n')

    # замена
    if repl != None:
        with open(path, 'w') as f:
            for line in new_data:
                f.write(line)

        with open(path, 'r') as f:
            for line in f.readlines():
                print(line, end='')


def write_to_file(path):
    if os.path.isfile(f'{path}'):
        print('Файл уже существует и будет перезаписан!')

    with open(path, 'w') as f:
        for i in zipped_list:
            f.write(f'{i[0]}, {i[1]}\n')

    read_file(path)


def read_file(path):
    with open(path, 'r') as f:
        for line in f.readlines():
            print(line, end='')


write_to_file(path)
find_it('5', 'QQQ')
