import random

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    numbers = list(range(lower, upper + 1))

    return sorted(random.sample(numbers, amount))


if __name__ == '__main__':
    for number in lottery_numbers(7, 1, 40):
        print(number)