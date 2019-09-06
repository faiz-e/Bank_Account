from User import User
from AccountNumber import AccountNumber
from CustomExceptions import InvalidAccountTypeException, InvalidAmountException


class UserAccountDetail:
    def __init__(self):
        """
        Constructor for creating BankAccountDetail object

        """
        self.__user = User()
        self.__acc_number = AccountNumber()
        self.__account_type = None
        self.__amount = 0.0

    def set_first_name(self, first_name):
        self.__user.first_name = first_name
        print("success")
        return self

    def set_last_name(self, last_name):
        self.__user.last_name = last_name
        print("success")

        return self

    def set_username(self, username):
        self.__user.username = username
        print("success")

        return self

    def set_password(self, password):
        self.__user.password = password
        print("success")

        return self

    def set_country_code(self, country_code):
        self.__acc_number.country = country_code
        print("success")

        return self

    def set_iban_check(self, iban_check):
        self.__acc_number.iban_check = iban_check
        print("success")

        return self

    def set_swift_code(self, swift_code):
        self.__acc_number.swift_code = swift_code
        print("success")

        return self

    def set_acc_number(self, acc_number):
        self.__acc_number.account_number = acc_number
        print("success")

        return self

    def user_details(self, first_name, last_name, username, password):
        self.__user = User(first_name, last_name, username, password)


    def account_number_details(self, country, iban_check, swift_code, acc_num):
        self.__acc_number = AccountNumber(country, iban_check, swift_code, acc_num)

    def set_account_type(self, acc_type):
        if acc_type.upper() == 'SAVINGS' or acc_type.upper() == 'CURRENT':
            self.__account_type = acc_type
            print("success")

        else:
            raise InvalidAccountTypeException("Account Type is invalid. Can be Current or Savings")
        return self

    def set_amount(self, amount):
        try:
            self.__amount = amount if isinstance(amount, float) else float(amount)
            print("success")

        except:
            raise InvalidAmountException("Amount is invalid")
        return self

    def get_first_name(self):
        return self.__user.first_name

    def get_last_name(self):
        return self.__user.last_name

    def get_username(self):
        return self.__user.username

    def get_password(self):
        return self.__user.password

    def get_country_code(self):
        return self.__acc_number.country

    def get_iban_check(self):
        return self.__acc_number.iban_check

    def get_swift_code(self):
        return self.__acc_number.swift_code

    def get_acc_number(self):
        return self.__acc_number.account_number

    def get_account_type(self):
        return self.__account_type

    def get_amount(self):
        return self.__amount

    def get_user(self):
        return self.__user

    def get_account_number(self):
        return self.__acc_number

    def build(self):
        print("success")

        return self
