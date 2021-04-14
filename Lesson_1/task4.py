"""
Написать программу «Банковский депозит».
Она должна состоять из функции и ее вызова с аргументами. Клиент банка делает депозит на определенный срок. 
В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых). 
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых). 
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых). 
Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада. 
Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24). 
Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока. 
В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет по нужной процентной ставке. 
Функция возвращает сумму вклада на конец срока.
"""

product_10k = {
    'begin_sum': 1000,
    'end_sum': 10000,
    '6': 5,
    '12': 6,
    '24': 5,
}
product_100k = {
    'begin_sum': 10001,
    'end_sum': 100000,
    '6': 6,
    '12': 7,
    '24': 6.5,
}
product_1m = {
    'begin_sum': 100001,
    'end_sum': 1000000,
    '6': 7,
    '12': 8,
    '24': 7.5,
}


def check_float(text=None):
    while True:
        data = input(text)
        if data.lstrip('-').replace('.', '', 1).isdigit() == False:
            print('\nПожалуйста, повторите ввод: нужно ввести натурально число')
        else:
            if data[0] == '-':
                data = data[0] + data.lstrip(data[0])
            return float(data)


def check_month(text=None):
    while True:
        data = input(text)
        if data not in ('6', '12', '24'):
            print('\nПожалуйста, повторите ввод: нужно ввести 6 или 12 или 24')
        else:
            return int(data)


def deposit(user_money, user_time):
    if user_money >= product_10k['begin_sum']:
        if user_money <= product_10k['end_sum']:
            val = product_10k[str(user_time)]
        if user_money >= product_100k['begin_sum']:
            if user_money <= product_100k['end_sum']:
                val = product_100k[str(user_time)]
        if user_money >= product_1m['begin_sum']:
            if user_money <= product_10k['end_sum']:
                val = product_1m[str(user_time)]

        return(round((user_money + ((user_money * val * ((user_time * 31) - (user_time / 2))) / (365 * 100))), 2))
    else:
        return 'Необходима сумма от 1 тысячи до 1 миллиона!'


user_money = check_float('Введите сумму: ')
user_time = check_month(
    'Выберите срок: 6 месяцев, 12 месяцев, 24 месяца (введите 6, 12 или 24): ')

print(deposit(user_money, user_time))
