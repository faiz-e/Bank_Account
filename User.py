# User class showing specifically bank users
import re
from Person import Person
from CustomExceptions import InvalidNameException


class User(Person):
    def __init__(self, first=None, last=None, username=None, password=None):
        """
        Constructor of User. Crate new User object
        :param first: First name of user
        :type first: str
        :param last:  Last name of user
        :type last: str
        :param username: username of user
        :type username: str
        :param password: password for the current user
        :type password: str
        """
        super().__init__(first, last)       # call to Person class constructor
        self.username = username
        self.password = password

    @property
    def username(self):
        """
        Return the username of user

        :return: username
        :rtype: str
        """
        return self.__username

    @username.setter
    def username(self, username):
        """
        Set the username of user

        :param username: Username of user
        :type username: str
        :return: None
        """
        if username is not None:
            if re.match(r"^[\w_-]{4,}$", username):
                self.__username = username
            else:
                raise InvalidNameException("Invalid Username. Must be atleast 4 characters longs &"
                                            " can only contain letters, numbers, hyphens, and underscore")
        else:
            self.__username = username

    @property
    def password(self):
        """
        Return the password for user

        :return: password of user
        :rtype: str
        """
        return self.__password

    @password.setter
    def password(self, password):
        """
        Set the password for user

        :param password: password for the user.
        :type password: str
        :return: None
        """
        if password is not None:
            if re.match(r".{6,}", password):
                self.__password = password
            else:
                raise InvalidNameException("Password must be at least 6 characters long")
        else:
            self.__password = password
