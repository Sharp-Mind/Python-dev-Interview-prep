"""
Реализовать расчет цены товара со скидкой.

Величина скидки должна передаваться в качестве аргумента в дочерний класс. 

Выполнить перегрузку методов конструктора дочернего класса 
(метод __init__, в который должна передаваться переменная — скидка), 
и перегрузку метода __str__ дочернего класса. 

В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.

Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы 
(вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, new_price):
        self.__price = new_price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, other, discount):
        self.parent_obj = other
        self.discount = discount

    def __str__(self):
        return str(round(self.get_parent_data(self.parent_obj)[1] * (1 - (self.discount / 100)), 2))

    def get_parent_data(self, other):
        return (other.get_name, other.get_price)


a = ItemDiscount('Холодильник', 15000)

b = ItemDiscountReport(a, 5)
b_pdata = b.get_parent_data(a)

print(f'Товар: {b_pdata[0]}, цена: {b_pdata[1]}')
print(f'Цена товара {b_pdata[0]} со скидкой: {b}')
