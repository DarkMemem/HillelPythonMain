import random
import string


def generate_password(length):
    low_upp = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.sample(low_upp, k=length))


def generate_password_specials(length):
    letters_and_specials = string.ascii_letters + string.digitspup
    rand_string = ''.join(random.sample(letters_and_specials, k=length))
    return rand_string


def generate_password_digits(length):
    symbol = '!"№;%:?*$()_+'
    letters_and_digits_specials = string.ascii_letters + symbol
    rand_string = ''.join(random.sample(letters_and_digits_specials, k=length))
    return rand_string


def generate_password_specials_digits(length):
    symbol = '!"№;%:?*$()_+'
    letters_and_digits = string.ascii_letters + string.digits + symbol
    rand_string = ''.join(random.sample(letters_and_digits, k=length))
    return rand_string
