"""
Разработать генератор случайных чисел. 
В функцию передавать начальное и конечное число генерации 
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""
from random import random

l1, d1 = [], {}
a, b = 25, 75


def give_me_num(a, b):
    def rand_num(a, b):
        yield round(random() * (b - a) + 1)
    for i in rand_num(a, b):
        return(i)


for el, order in enumerate(range(b - a)):
    num = give_me_num(a, b)
    l1.append(num)
    d1[f'elem_{order}'] = num

print(f'\n{l1}\n\n{d1}')
