from item_base import *
from order_details import *
from admin import *

user_1 = User('Ivan', 'Niciforov', 8999996)
user_2 = User('Elizaveta', 'Ugodina', 8999559)
user_3 = User('Roman', 'Romanov', 89993259)
user_4 = User('Tatyana', 'Pavlovna', 89921499)
user_5 = User('Georgiy', 'Ivanov', 89925699)

Item_Database.distribution_of_items()

admin = Administrator('Evgeniy', 'Voloshanin')
admin.add_item('car', 'bmv', 5000000)

OrderDetails.add_to_cart('Ivan', 8999996)

# ССЫЛКА НА UML
# https://disk.yandex.ru/i/AwLo8Rbzb-A2HA


