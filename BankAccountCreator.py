# BankAccount class

from Account import Account
from abc import ABC, abstractclassmethod


class BankAccountCreator(ABC):
    def __init__(self):  # , user_obj, acc_number_obj, account_type, amount=0.0):
        pass

    @abstractclassmethod
    def create_account(self, user_account_details):
        """
        Create new account based on user choice . Saving or Current

        :param user_account_details: Details of the account to be created
        :type user_account_details: AccountDetails
        :return: Saving object or Current object
        :rtype: Account

        """
        pass

