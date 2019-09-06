# This file contains all custom exceptions used in the project


class InvalidAccountTypeException(Exception):
    """ Exception will be raised if user provides invalid Account type name"""
    pass


class NotEnoughAmountException(Exception):
    """ Exception will be raised if users passes Invalid Amount"""
    pass


class InvalidAmountException(Exception):
    """ Exception will be raised if users passes Incorrect Amount"""
    pass


class InvalidCountryCode(Exception):
    """ Country Code Exception """
    pass


class InvalidIBANCheckCodeException(Exception):
    """ Invalid International Bank Account Number Check Code Exception"""
    pass


class InvalidSwiftCodeException(Exception):
    """ Invalid SWIFT/BIC Code Exception"""
    pass


class InvalidAccountNumberException(Exception):
    """ Invalid Account Number Exception"""
    pass


class InvalidNameException(Exception):
    """Exception will be raised if any name is invalid"""
    pass


class UserAlreadyExistException(Exception):
    """Exception will be raised if username is already registered"""
    pass