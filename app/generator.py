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

