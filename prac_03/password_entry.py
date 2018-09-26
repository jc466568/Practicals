""" Elwyn Omanga """


def main():
    password = input("Enter a password 10 or more characters long: ")
    while not check_password(password):
        password = input("Enter a valid password: ")
    print('*'*len(password))


def check_password(password):
    if len(password) >= 10:
        return True


main()
