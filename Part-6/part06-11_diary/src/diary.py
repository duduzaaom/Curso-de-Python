def write_diary(text: str):
    with open('diary.txt', 'a') as file:
        file.write(text + '\n')


def read_diary():
    with open('diary.txt') as file:
        for line in file:
            print(line.strip())


def main():
    while True:
        print('1 - add an entry, 2 - read entries, 0 - quit')
        function = int(input('Function: '))

        if function == 1:
            diary_entry = input('Diary entry: ')
            write_diary(diary_entry)
            print('Diary saved')
        elif function == 2:
            read_diary()
        elif function == 0:
            print('Bye now!')
            break


main()