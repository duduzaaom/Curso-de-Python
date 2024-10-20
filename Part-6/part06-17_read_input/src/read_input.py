def read_input(input_text: str, min_number: int, max_number: int) -> int:
    while True:
        try:
            number = int(input(f'{input_text}'))
            if number > min_number and number < max_number:
                return number
        except ValueError:
            pass

        print(f'You must type in an integer between {min_number} and {max_number}')


if __name__ == '__main__':
    number = read_input("Please type in a number: ", 1, 5)
    print("You typed in:", number)