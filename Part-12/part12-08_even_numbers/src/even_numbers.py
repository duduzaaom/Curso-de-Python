def even_numbers(beginning: int, maximum: int):
    for number in range(beginning, maximum + 1):
        if number % 2 == 0:
            yield number


if __name__ == "__main__":
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)
    
