"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс
ItemDiscountReport на два класса. Инициализировать классы необязательно. 

Внутри каждого поместить функцию get_info, которая в первом классе будет 
отвечать за вывод названия товара, а вторая — его цены. 
Далее реализовать выполнение каждой из функции тремя способами.
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

    # 1-й способ:
    @property
    def get_info(self):
        return self.get_parent_data(self.parent_obj)[0]

    # 2-й способ:
    # def get_info(self, other):
    #     return self.get_parent_data(other)[0]

    # 3-й способ:
    # def get_info(self, other):
    #     return other.get_name


class ItemDiscountReportVer2(ItemDiscountReport):
    # 1-й способ:
    @property
    def get_info(self):
        return self.get_parent_data(self.parent_obj)[1]

    # 2-й способ:
    # def get_info(self, other):
    #     return self.get_parent_data(other)[1]

    # 3-й способ:
    # def get_info(self, other):
    #     return other.get_price


a = ItemDiscount('Холодильник', 15000)

b = ItemDiscountReport(a, 5)
b_pdata = b.get_parent_data(a)

print(f'Товар: {b_pdata[0]}, цена: {b_pdata[1]}')
print(f'Цена товара {b_pdata[0]} со скидкой: {b}')

c = ItemDiscountReportVer2(a, 5)
# вывод для 1-го способа:
print(c.get_info)
# вывод для 2-го и 3-го способов:
# print(c.get_info(a))
