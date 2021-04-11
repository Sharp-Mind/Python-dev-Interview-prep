"""
Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
(функция, отвечающая за отображение информации о товаре в одной строке).
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
    def get_parent_data(self):
        print(f'Товар: {self.get_name}, цена: {self.get_price}')


a = ItemDiscount('Холодильник', 15000)
b = ItemDiscountReport
b.get_parent_data(a)

a.set_price(14000)
b.get_parent_data(a)
