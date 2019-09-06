# Saving account will be a type of account
from CustomExceptions import NotEnoughAmountException, InvalidAmountException
from Account import Account
from User import User
from AccountNumber import AccountNumber


class Saving(Account):
    def __init__(self, user_obj, acc_number_obj, amount=0.0):
        """
        Create new Current object.

        :param user_obj: Contains Account holder details
        :type user_obj: User
        :param acc_number_obj: Contains Account number details
        :type acc_number_obj: AccountNumber
        :param amount: Amount to store in the account
        :type amount: float
        """
        super().__init__(user_obj=user_obj, acc_number_obj=acc_number_obj)
        self.deposit_amount(amount)

    # Abstract method overloaded
    def withdraw_amount(self, amount):
        """
        Withdraw amount from current account
        :param amount:
        :return:
        """
        if isinstance(amount, float) and amount > 0.0:  # if amount is a positive float number
            if self._amount > amount + amount * (2/100):       # if enough amount is present in account
                self._amount -= (amount + amount * (2/100))       # add that amount to account totals
                return self._amount
            else:
                raise NotEnoughAmountException("Current Amount is not Enough to withdraw")
        else:
            raise InvalidAmountException("Your Inputted Amount is invalid")
