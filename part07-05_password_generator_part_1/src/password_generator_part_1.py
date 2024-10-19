from string import ascii_lowercase
from random import randint

def generate_password(length: int) -> str:
    password = ''
    for i in range(length):
        password += ascii_lowercase[randint(0, 25)]

    return password


if __name__ == '__main__':
    for i in range(10):
        print(generate_password(8))