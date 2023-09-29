from item import *


class Item_Database:
    def __init__(self):
        self._items = [
            {
                'category': 'car',
                'tittle': 'Honda',
                'price': 2000000
            },

        ]

    @property
    def baza_items(self):
        return self._items

    @baza_items.getter
    def distribution_of_items(self):
        for i in range(len(self._items)):
            Item(self._items[i].get('Catecory'), self._items[i].get('Tittle'), self._items[i].get('price'))








