import random
import string


def generate_password(length, specials, digits):
    base_random = string.ascii_lowercase
    if specials == 1:
        base_random += string.punctuation

    if digits == 1:
        base_random += string.digits

    password = ''.join(random.sample(base_random, length))
    return password
