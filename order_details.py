from order import *
from item import *


class OrderDetails:
    __list_order = dict()

    @staticmethod
    def add_to_cart(user_name, user_phone):
        print('___Добавьте товар в корзину___')
        Order.get_user_tittle(user_name, user_phone)
        if Order.get_user_tittle != None:
            if Order.get_user_tittle in Item.get_item_by_tittle:
                if not Order.get_user_tittle in OrderDetails.__list_order:
                    OrderDetails.__list_order[Order.get_user_tittle] = (Item.get_item_by_price(Order.get_user_tittle))


    @property
    def list_order(self):
        return self.__list_order

    @list_order.getter
    def get_order(self):
        return self.__list_order
    # далее можно реализовать оплату

