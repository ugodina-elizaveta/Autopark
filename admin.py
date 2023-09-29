from user import*
from item import *


class Administrator(User):
    __last_id = 0

    def __init__(self, name, surname):
        Administrator.__last_id += 1
        super().__init__(self, name, surname)

    def add_item(self, item_category, item_name, item_price):
        Item(item_category, item_name, item_price)

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.surname

