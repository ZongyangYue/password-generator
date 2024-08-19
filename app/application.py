import string
from secrets import randbelow

def generate(length: int):
    charpool = string.ascii_lowercase

    charpool_length = len(charpool)
    password = ''

    for _ in range(length):
        password = f'{password}{charpool[randbelow(charpool_length)]}'

    return password
# reference: https://github.com/kanish671/ranpass/blob/main/app/application.py