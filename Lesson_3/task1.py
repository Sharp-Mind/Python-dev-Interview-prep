"""
 Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
 При вызове функции в качестве аргумента должно передаваться имя файла с расширением. 
 В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
 """

import os

some_file = 'test.txt'


def get_filename(file):
    parts = []
    os.chdir(os.path.abspath(file).rstrip(file))
    while os.getcwd() != '/':        
        parts.insert(0, f'{os.getcwd().split("/")[-1]}/')
        os.chdir("..")
    parts.insert(0, '/')
    parts.append(file)
    return ''.join(parts).split('/')[-1].split('.')[0]


print(get_filename(some_file))
