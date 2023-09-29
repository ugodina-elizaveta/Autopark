from user import *
from random import randint


class Order:
    __last_id = 0

    def __init__(self):
        Order.__last_id += 1
        self.id = Order.__last_id
        self.created = datetime.datetime.now()
        self.updated = None
        self.last_visit = self.created

    @staticmethod
    def get_user_tittle(user_name, user_phone):
        kod = randint(1000, 9999)
        if not user_name == User.get_user_by_phone(user_phone):
            User.get_user_by_phone(user_phone)
        elif input('Подтвердите свою личность. Для этого введите код, который мы выслали Вам на номер телефона:') == print(kod):
            print('Личность подтверждена')
            print('Введите через запятую товары, которые Вы хотите добавить в корзину:')
            _user_tittle = input()

            return _user_tittle




