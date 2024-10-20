year = int(input('Year: '))
leap_year = year

while True:
    leap_year += 1

    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            break
    else:
        if leap_year % 4 == 0:
            break

print(f'The next leap year after {year} is {leap_year}')