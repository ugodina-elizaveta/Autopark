import datetime


class User:
    __last_id = 0
    __list_user = dict()

    def __init__(self, name, surname, phone):
        User.__last_id += 1
        self.id = User.__last_id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.created = datetime.datetime.now()
        self.updated = None
        self.last_visit = self.created
        User.__list_user[User.__last_id] = self

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @staticmethod
    def get_user_by_id(id):
        for user in User.__list_user:
            if user.id == id:
                return user
        raise ValueError('Пользователь не найден')

    @staticmethod
    def get_user_by_phone(phone):
        for user in User.__list_user:
            if user.phone == phone:
                return user
        raise ValueError('Пользователь не найден')

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.surname


