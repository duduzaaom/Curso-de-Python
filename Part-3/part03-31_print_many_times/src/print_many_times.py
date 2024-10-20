def print_many_times(text, times):
    count = 1

    while count <= times:
        print(text)

        count += 1

if __name__ == "__main__":
    print_many_times("python", 5)