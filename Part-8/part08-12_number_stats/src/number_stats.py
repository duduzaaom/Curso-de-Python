class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers) if self.numbers != [] else 0
    
    def average(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers != [] else 0


all_numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()
print("Please type in integer numbers:")
while True:
    number = int(input())
    if number == -1:
        break
    
    if number % 2 == 0:
        even_numbers.add_number(number)
    else:
        odd_numbers.add_number(number)

    all_numbers.add_number(number)
    
print(f"Sum of numbers: {all_numbers.get_sum()}")
print(f"Mean of numbers: {all_numbers.average()}")
print(f"Sum of even numbers: {even_numbers.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers.get_sum()}")

