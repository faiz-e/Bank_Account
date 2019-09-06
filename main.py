# main user program. Custom user program, allowed editing here by user

from Database import Database
from UserAccountDetail import UserAccountDetail
from UserDetail import UserDetail
from CustomExceptions import UserAlreadyExistException

def user_details_input(what_to_set):
    method_matcher = {
        'first_name': 'First Name\t: ',
        'last_name': 'Last Name\t: ',
        'username': 'Username\t: ',
        'password': 'Password\t: ',
    }
    
    while True:  # while user don't enter valid input data
        try:
            data = input(method_matcher[what_to_set])  # print the corresponding prompt message
            if what_to_set == 'first_name':
                user_details.set_first_name(data); break
            elif what_to_set == 'last_name':
                user_details.set_last_name(data); break
            elif what_to_set == 'username':
                user_details.set_username(data); break
            elif what_to_set == 'password':
                user_details.set_password(data); break
            else:
                raise KeyError # if key was not found
        except Exception as exception:
            print(exception)


def user_account_details_input(what_to_set):
    method_matcher = {
        'first_name': 'First Name\t: ',
        'last_name': 'Last Name\t: ',
        'username': 'Username\t: ',
        'password': 'Password\t: ',
        'country': 'Country\t: ',
        'iban': 'IBAN Code\t:',
        'swift': 'Swift Code\t: ',
        'acc_num': 'Account Number(16 Digits)\t :',
        'acc_type': 'Account Type(Current | Savings)\t :',
        'init_amount': 'Initial Amount\t :'
    }

    while True:  # while user don't enter valid input data
        try:
            data = input(method_matcher[what_to_set])  # print the corresponding prompt message
            if what_to_set == 'first_name':
                user_account_details.set_first_name(data); break
            elif what_to_set == 'last_name':
                user_account_details.set_last_name(data); break
            elif what_to_set == 'username':
                user_account_details.set_username(data); break
            elif what_to_set == 'password':
                user_account_details.set_password(data); break
            elif what_to_set == 'country':
                user_account_details.set_country_code(data); break
            elif what_to_set == 'iban':
                user_account_details.set_iban_check(data); break
            elif what_to_set == 'swift':
                user_account_details.set_swift_code(data); break
            elif what_to_set == 'acc_num':
                user_account_details.set_acc_number(data); break
            elif what_to_set == 'acc_type':
                user_account_details.set_account_type(data); break
            elif what_to_set == 'init_amount':
                user_account_details.set_amount(data); break
            else:
                raise KeyError # if key was not found
        except Exception as exception:
            print(exception)


if __name__ == '__main__':
    try:
        database = Database()
        is_logged_in = False
        while not is_logged_in:  # While user don't login, keep running this code
            user_details = UserDetail()
            print("""
            1- Admin Login
            2- Admin SignUp
            3- Exit""")
            choice = input(">> ")
            if choice == '1':
                username = input("\tUsername    :")
                password = input("\tPassword    :")
                if database.read_user_data(username) is None:
                    print("User Not Found")
                else:
                    user_details = database.read_user_data(username)
                    print("LOGIN SUCCESSFUL\n")
                    is_logged_in = True
            elif choice == '2':

                user_details_input('first_name')
                user_details_input('last_name')
                user_details_input('username')
                user_details_input('password')
                try:
                    database.write_user_data(user_details)
                    print("Successfully Registered. Login to continue")
                except UserAlreadyExistException as e:
                    print(e)

            elif choice == '3':
                print("Thank You For Using our services")
                exit(0)
            else:
                print("Invalid Input. Try Again")

        if is_logged_in:  # meaning user(admin) has logged in and can use the program now

            user_account_details = UserAccountDetail()
            while True:
                print("""
                1- Create New Bank Account
                2- Use existing Bank Account
                3- Logout
                """)

                choice = input(">> ")

                if choice == '1':
                    user_account_details_input('first_name')
                    user_account_details_input('last_name')
                    user_account_details_input('username')
                    user_account_details_input('password')
                    user_account_details_input('country')
                    user_account_details_input('iban')
                    user_account_details_input('swift')
                    user_account_details_input('acc_num')
                    user_account_details_input('acc_type')
                    user_account_details_input('init_amount')

                    try:
                        database.write_account_data(user_account_details)
                        print("Successfully Registered. Login to get more options")
                    except UserAlreadyExistException as e:
                        print(e)

                elif choice == '2':
                    username = input("Username\t")
                    password = input("Password\t")
                    if database.read_account_data(username) is None:
                        print("Username not found")
                    else:
                        user_account_details = database.read_account_data(username)
                        print("SuccessFull Login.")

                elif choice == '3':
                    exit(0)
                else:
                    print("Invalid Input. Try Again")
    except Exception as e:
        print(e)