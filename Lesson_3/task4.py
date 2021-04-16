"""
4. Написать программу, в которой реализовать две функции.

В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл.

Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""

import os
import string
from random import randint, choice


letters = string.ascii_letters

list_a = [f'{choice(letters)}{choice(letters)}' for _ in range(10)]
list_b = [randint(1, 100) for _ in range(10)]
zipped_list = list(zip(list_a, list_b))

path = "/home/user/test.txt"


def write_to_file(path):
    if os.path.isfile(f'{path}'):
        print('Файл уже существует и будет перезаписан!')

    with open(f'{path}', 'w') as f:
        for i in zipped_list:
            f.write(f'{i[0]}, {i[1]}\n')

    read_file(path)


def read_file(path):
    with open(f'{path}', 'r') as f:
        for line in f.readlines():
            print(line, end='')


write_to_file(path)
