"""
3. Создать два списка с различным количеством элементов.

В первом должны быть записаны ключи, во втором — значения. 
Необходимо написать функцию, создающую из данных ключей и значений словарь. 

Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""
from random import randint, choice
import string

letters = string.ascii_letters

list_a = [f'{choice(letters)}{choice(letters)}' for _ in range(9)]
list_b = [randint(1, 100) for _ in range(10)]
out_dict = {}

difference = len(list_a) - len(list_b)

if difference > 0:
    for _ in range(difference):
        list_b.append(None)
elif difference < 0:
    for _ in range(difference):
        list_a.pop()


zipped_list = list(zip(list_a, list_b))

print(
    f'Первый список: {list_a}\nВторой список: {list_b}\nСовмещённый список: {zipped_list}\n')


print(
    f'Словарь: {dict(zipped_list)},\nРазмер словаря: {len(dict(zipped_list))}')
