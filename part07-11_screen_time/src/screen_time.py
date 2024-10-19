from datetime import datetime, timedelta

if False:
    filename = input('Filename: ')
    input_date = input('Starting date: ')
    days = int(input('How many days: '))
else:
    filename = "late_june.txt"
    input_date = '24.6.2020'
    days = 5

starting_date = datetime.strptime(input_date, "%d.%m.%Y")

print('Please type in screen time in minutes on each day (TV computer mobile):')
for day in range(days):
    current_date = starting_date + timedelta(days=day)
    screen_time = input(f'Screen time {current_date.strftime('%d.%m.%Y')}: ')