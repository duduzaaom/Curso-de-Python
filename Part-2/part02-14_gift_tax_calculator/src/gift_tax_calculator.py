value = int(input('Value of gift: '))

tax = 0
tax_rate = 0
tax_lower = 0
lower_limit = 0

if value < 5000:
    tax = 0
elif value < 25000:
    lower_limit = 5000
    tax_lower = 100
    tax_rate = 0.08
elif value < 55000:
    lower_limit = 25000
    tax_lower = 1700
    tax_rate = 0.1
elif value < 200000:
    lower_limit = 55000
    tax_lower = 4700
    tax_rate = 0.12
elif value < 1000000:
    lower_limit = 200000
    tax_lower = 22100
    tax_rate = 0.15
else:
    lower_limit = 1000000
    tax_lower = 142100
    tax_rate = 0.17

tax = tax_lower + (value - lower_limit) * tax_rate

if tax == 0:
    print('No tax!')
else:
    print(f'Amount of tax: {tax} euros')
