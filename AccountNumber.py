# Account Number class for the account number of bank users
import re
from CustomExceptions import InvalidCountryCode, InvalidSwiftCodeException, InvalidIBANCheckCodeException, InvalidAccountNumberException

class AccountNumber:
    def __init__(self, country=None, iban_check=None, swift_code=None, acc_num=None):
        """
        Create new AccontNumber object.

        :param country: country
        :type country: str
        :param iban_check: International Bank Account Number (IBAN) Check code
        :type iban_check: int
        :param swift_code: SWIFT/BIC Code for the Account. Must be Only 4 Characters.
        :type swift_code: str
        :param acc_num: Account number of the account
        :type acc_num: str
        """
        self.country = country
        self.iban_check = iban_check
        self.swift_code = swift_code
        self.account_number = acc_num

    @property
    def country(self):
        """
        Return the country of Account Number

        :return: Country
        :rtype: str
        """
        return self.__country

    @country.setter
    def country(self, country):
        """
        Set the country of Account Number

        :param country: country
        :type country: str
        :return: None
        """
        if country is not None:
            if re.match(r"^[A-Za-z]{2}$", country):
                self.__country = country.upper()
            else:
                raise InvalidCountryCode("Invalid Country Code. MUST contain only 2 digits")
        else:
            self.__country = country

    @property
    def iban_check(self):
        """
        Return the International Bank Account Number (IBAN) Check code

        :return: IBAN Check code
        :rtype: int
        """
        return self.__IBAN_check

    @iban_check.setter
    def iban_check(self, iban_check):
        """
        Set the International Bank Account Number (IBAN) Check code. 2 digits long.

        :param iban_check: International Bank Account Number (IBAN) Check code
        :type iban_check: int
        :return: None
        """
        if iban_check is not None:
            if re.match(r"^\d{2}$", str(iban_check)):
                self.__IBAN_check = iban_check
            else:
                raise InvalidIBANCheckCodeException("Invalid IBAN CHECK CODE. Must Only Contain 2 digits")
        else:
            self.__IBAN_check = iban_check

    @property
    def swift_code(self):
        """
        Return the SWIFT/BIC Code for the Account

        :return: SWIFT/BIC Code for the Account
        :rtype: str
        """
        return self.__swift_code

    @swift_code.setter
    def swift_code(self, swift_code):
        """
        Set the 4 Character long SWIFT/BIC Code for the account.

        :param swift_code: SWIFT/BIC Code for the Account. Must be Only 4 Characters.
        :type swift_code: str
        :return: None
        """
        if swift_code is not None:
            if re.match(r"^[a-zA-Z]{4}$", swift_code):
                self.__swift_code = swift_code.upper()
            else:
                raise InvalidSwiftCodeException("SWIFT/BIC Code is Invalid. Must only contain 4 Characters")
        else:
            self.__swift_code = swift_code

    @property
    def account_number(self):
        """
        Return the Local Account Number of the Account

        :return: Account Number of length 16
        :rtype: str
        """
        return self.__account_number

    @account_number.setter
    def account_number(self, acc_num):
        """
        Set the Local Account Number of the Account

        :param acc_num: Account number of the account
        :type acc_num: str
        :return: None
        """
        if acc_num is not None:
            if re.match(r"^[\w]{16}$", acc_num):
                self.__account_number = acc_num
            else:
                raise InvalidAccountNumberException("Invalid ACC Number. Must be 16 Characters Long.")
        else:
            self.__account_number = acc_num

    def __str__(self):
        return f"""
        {self.country} {self.iban_check} {self.swift_code} {self.account_number}
        """
