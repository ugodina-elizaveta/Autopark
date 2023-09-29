import datetime


class Item:
    __last_id = 0
    __list_item = dict()

    def __init__(self, category, tittle, price):
        Item.__last_id += 1
        self.id = Item.__last_id
        self.tittle = tittle
        self.price = price
        self.created = datetime.datetime.now()
        self.updated = None
        self.category = category
        Item.__list_item[Item.__last_id] = self

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @staticmethod
    def get_item_by_id(id):
        for item in Item.__list_item:
            if item.id == id:
                return item
        raise ValueError('Товар не найден')

    @staticmethod
    def get_item_by_price(price):
        for product in Item.__list_item:
            if product.price == price:
                return price
        raise ValueError('Товар не найден')

    @staticmethod
    def get_item_by_tittle(tittle):
        for item in Item.__list_item:
            if item.tittle == tittle:
                return item
        raise ValueError('Товар не найден')

    def __str__(self):
        return str(self.id) + ' ' + self.category + ' ' + self.tittle + ' ' + str(self.price)