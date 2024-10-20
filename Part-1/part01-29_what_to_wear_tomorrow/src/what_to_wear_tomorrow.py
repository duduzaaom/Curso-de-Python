print('What is the weather forecast for tomorrow?')
temperature = int(input('Temperature: '))
rain = input('Will it rain (yes/no): ')
check = 0

if temperature > 20:
    print('Wear jeans and a T-shirt')

if temperature <= 20:
    check += 1

if temperature <= 10:
    check += 1

if temperature <= 5:
    check += 1

if check == 1:
    print('Wear jeans and a T-shirt')
    print('I recommend a jumper as well')

if check == 2:
    print('Wear jeans and a T-shirt')
    print('I recommend a jumper as well')
    print('Take a jacket with you')

if check == 3:
    print('Wear jeans and a T-shirt')
    print('I recommend a jumper as well')
    print('Take a jacket with you')
    print('Make it a warm coat, actually')
    print('I think gloves are in order')

if rain == 'yes':
    print("Don't forget your umbrella!")
