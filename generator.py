import random
from string import ascii_letters, punctuation, digits


# character list containing lower and upper case letters, punctuation
# symbols and digits from 0 to 9
character_list = list(ascii_letters) + list(punctuation) + list(map(str, digits))


def generate_password(password_length):
    """
    Resposible for generating the passwords.
    :param password_length: integer
    :return: a password
    """
    password = ""
    character_list_size = len(character_list)

    for i in range(password_length):
        character = random.randint(0, character_list_size-1)
        password += character_list[character]

    return password


def multiple_passwords(number_of_passwords, password_length):
    """
    Resposible for generating multiple passwords
    if user needs more than one
    :param number_of_passwords: integer
    :param password_length: integer
    :return: list containing more than one password
    """

    password_list = [generate_password(password_length) for i in range(number_of_passwords)]
    return password_list


if __name__ == "__main__":
    length = 8
    print(generate_password(length))

    length = 16
    password_number = 3
    print(multiple_passwords(password_number, length))

    length = 16
    print(generate_password(length))

    length = 8
    password_number = 2
    print(multiple_passwords(password_number, length))
