def is_prime(number: int):
    for n in range(2, number):
        if number % n == 0:
            return False
        
    return True


def prime_numbers():
    number = 2
    while True:
        if is_prime(number):
            yield number

        number += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
