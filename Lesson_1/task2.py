# Дополнить следующую функцию недостающим кодом:
# def print_directory_contents(sPath):
#     """
#     Функция принимает имя каталога и распечатывает его содержимое
#     в виде «путь и имя файла», а также любые другие
#     файлы во вложенных каталогах.

#     Эта функция подобна os.walk. Использовать функцию os.walk
#     нельзя. Данная задача показывает ваше умение работать с
#     вложенными структурами.
#     """
#     # заполните далее
import os


def print_directory_contents(sPath):
    if os.path.exists(sPath):
        if os.path.isdir(sPath):
            objs = []
            for i in os.listdir(sPath):
                if os.path.isdir(os.path.join(sPath, i)):
                    print_directory_contents(os.path.join(sPath, i))
                objs.append(i)
            for i in sorted(objs):
                print(os.path.join(sPath, i))


print_directory_contents(r"C:\Users\user\Documents")
