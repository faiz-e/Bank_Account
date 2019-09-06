from User import User


class UserDetail:
    def __init__(self):
        """
        Constructor for creating BankAccountDetail object

        """
        self.__user = User()

    def set_first_name(self, first_name):
        self.__user.first_name = first_name
        return self

    def set_last_name(self, last_name):
        self.__user.last_name = last_name
        return self

    def set_username(self, username):
        self.__user.username = username
        return self

    def set_password(self, password):
        self.__user.password = password
        return self

    def get_first_name(self):
        return self.__user.first_name

    def get_last_name(self):
        return self.__user.last_name

    def get_username(self):
        return self.__user.username

    def get_password(self):
        return self.__user.password

    def user_details(self, first_name, last_name, username, password):
        self.__user = User(first_name, last_name, username, password)

    def build(self):
        return self

