def read_fruits():
    with open('fruits.csv') as file:
        fruits_price = {}
    
        for line in file:
            line = line.replace('\n', '')
            parts = line.split(';')

            fruits_price[parts[0]] = float(parts[1])

    return fruits_price


