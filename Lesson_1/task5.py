"""
Усовершенствовать программу «Банковский депозит». 
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада. 
Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы. 
Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего. 
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. 
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), 
а главная функция — общую сумму по вкладу на конец периода.
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


def deposit(user_money, user_time, user_add=0):

    if user_add > 0:
        add_money = user_add

    if user_money >= product_10k['begin_sum']:
        if user_money <= product_10k['end_sum']:
            val = product_10k[str(user_time)]
        if user_money >= product_100k['begin_sum']:
            if user_money <= product_100k['end_sum']:
                val = product_100k[str(user_time)]
        if user_money >= product_1m['begin_sum']:
            if user_money <= product_10k['end_sum']:
                val = product_1m[str(user_time)]
    else:
        return 'Необходима сумма от 1 тысячи до 1 миллиона!'

    def capital(user_money, user_time, user_add):
        total = 0
        for _ in range(user_time):
            total += user_add * (((1 + ((val) * (((user_time - 2) * 31) -
                                                 ((user_time - 2) / 2)) / (365 * 100)))) ** user_time) - user_add
            user_add += add_money
        return total

    additional_money = round(capital(user_money, user_time, user_add), 2)
    user_money += additional_money

    return(round((user_money + ((user_money * val * ((user_time * 31) - (user_time / 2))) / (365 * 100))), 2)), additional_money


user_money = check_float('Введите сумму: ')
user_time = check_month(
    'Выберите срок: 6 месяцев, 12 месяцев, 24 месяца (введите 6, 12 или 24): ')

print(deposit(user_money, user_time, 2000))
