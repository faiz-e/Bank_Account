from BankAccountCreator import BankAccountCreator
from Saving import Saving
from Current import Current
from CustomExceptions import InvalidAccountTypeException
from abc import abstractclassmethod


class AccountCreator(BankAccountCreator):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_account(cls, user_account_details):
        try:

            if user_account_details.get_account_type().upper() == 'SAVINGS':
                return Saving(user_account_details.get_user(), user_account_details.get_account_number(), user_account_details.get_amount())
            elif user_account_details.get_account_type().upper() == 'CURRENT':
                return Current(user_account_details.get_user(), user_account_details.get_account_number(), user_account_details.get_amount())
            else:
                raise InvalidAccountTypeException("Account Type is invalid. Can be Current or Savings")
        except InvalidAccountTypeException as e:
            print(e)
    # def create_account(self, user_obj, acc_number_obj, account_type, amount=0.0):
    #     if account_type.upper() == 'SAVINGS':
    #         return Saving(user_obj, acc_number_obj, amount)
    #     elif account_type.upper() == 'CURRENT':
    #         return Current(user_obj, acc_number_obj, amount)
    #     else:
    #         raise InvalidAccountTypeException("Account Type is invalid. Can be Current or Savings")
