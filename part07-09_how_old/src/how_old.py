from datetime import datetime

day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

birth_date = datetime(year, month, day)
eve_millennium_date = datetime(1999, 12, 31)
difference = eve_millennium_date - birth_date

if year >= 2000:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
