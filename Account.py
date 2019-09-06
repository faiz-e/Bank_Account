# General Class indicating user bank Account
from abc import ABC, abstractmethod

from User import User
from AccountNumber import AccountNumber
from CustomExceptions import InvalidAmountException

class Account(ABC):
    def __init__(self, user_obj, acc_number_obj):
        """
        Constructor of Account class. Create new Account object.

        :param user_obj: Contains Account holder details
        :type user_obj: User
        :param acc_number_obj: Contains Account number details
        :type acc_number_obj: AccountNumber
        """
        super().__init__()      # for the ABC class
        self.account_holder = user_obj     # for User
        self.account_number = acc_number_obj    # for AccountNumber
        self._amount = 0.0

    @property
    def _amount(self):
        """
        Protected method which return the current amount

        :return: current Amount
        :rtype: float
        """
        return self.__amount

    @_amount.setter
    def _amount(self, amount):
        """
        Protected method to set the current amount

        :param amount: new amount
        :type amount: float
        :return: None
        """
        self.__amount = amount

    @property
    def account_holder(self):
        """
        Return Details of Account Holder

        :return: Account Holder details
        ":rtype: User
        """
        return self.__account_holder

    @account_holder.setter
    def account_holder(self, acc_holder):
        """
        Set Details of the Account Holder (user)

        :param acc_holder: Details of Account Holder(user)
        :type acc_holder: User
        :return: None
        """
        self.__account_holder = acc_holder

    @property
    def account_number(self):
        """
        Return Account Number of Account

        :return: Account Number of Account
        :rtype: AccountNumber
        """
        return self.__account_number

    @account_number.setter
    def account_number(self, acc_number):
        """
        Set the account number of the account

        :param acc_number: Account Number of Account
        :type acc_number: AccountNumber
        :return: None
        """
        self.__account_number = acc_number

    @abstractmethod
    def withdraw_amount(self, amount):
        """
        Withdraw the amount user wants from current amount.

        :param amount: Amount user wants to withdraw from account
        :type amount: float
        :return: Remaining amount left in acount
        :rtype: float
        """
        pass

    def deposit_amount(self, amount):
        """
        Deposit the amount user provides to his account.

        :param amount: Amount user wants to deposit
        :type amount: float
        :return: Return the total amount after deposit
        :rtype: float
        """
        if isinstance(amount, float) and amount > 0.0:  # if amount is a positive float number
            self._amount += amount
            return self._amount
        else:
            raise InvalidAmountException("Your Inputted Amount is Invalid")
