def check_line(line: str):
    separate_line = line.split(';')
    separate_weekinfo = separate_line[0].split()
    try:
        week_number = int(separate_weekinfo[1])
    except ValueError:
        return False

    lottery_numbers = []

    if len(separate_line[1].split(',')) < 7:
        return False

    for number in separate_line[1].split(','):
        try:
            number = int(number)
        except ValueError:
            return False

        if number in lottery_numbers or number < 1 or number > 39:
            return False

        lottery_numbers.append(number)

    return True


def filter_incorrect():
    with open('lottery_numbers.csv') as complete_file, open('correct_numbers.csv', 'w') as correct_file:
        for line in complete_file:
            line = line.strip()
            if check_line(line):
                correct_file.write(line + '\n')


if __name__ == '__main__':
    filter_incorrect()