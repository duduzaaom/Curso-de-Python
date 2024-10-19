def line(length, string):
    if string != '':
        print(string[0] * length)
    else:
        print('*' * length)

if __name__ == "__main__":
    line(5, "LOL")