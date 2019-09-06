# Person class indicating general persons
import re
from CustomExceptions import InvalidNameException


class Person:
    def __init__(self, first=None, last=None):
        """
        Create new Person object.

        :param first: First name of user
        :type first: str
        :param last:  Last name of user
        :type last: str
        """
        self.first_name = first
        self.last_name = last

    @property
    def first_name(self):
        """
        Return the first name of the person

        :return:First name of person
        :rtype: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, first):
        """
        Set the first name of the person. Must only contain characters a-z A-Z

        :param first: First name of the person
        :type first: str
        :return: None
        """

        if first is not None:

            if re.match(r"^[a-zA-Z]{2,}$", first):
                self.__first_name = first
            else:
                raise InvalidNameException("First Name should only contain letters")
        else:
            self.__first_name = first

    @property
    def last_name(self):
        """
        Return the last name of the person

        :return:last name of person
        :rtype: str
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, last):
        """
        Set the last name of the person. Must only contain characters a-z A-Z

        :param last: Last name of the person
        :type last: str
        :return: None
        """
        if last is not None:
            if re.match(r"^[a-zA-Z]{2,}$", last):
                self.__last_name = last
            else:
                raise InvalidNameException("Last Name should only contain letters")
        else:
            self.__last_name = last

    def __str__(self):
        return f"""
        First Name : {self.__first_name}
        Last Name  : {self.__last_name}
        """
