#import sys


def exchange(numbers, index):
    temp_numbers = numbers[index +1:]
    temp_numbers += numbers[:index + 1]
    
    return temp_numbers

numbers = input()
index = input()

print(exchange(numbers, index))