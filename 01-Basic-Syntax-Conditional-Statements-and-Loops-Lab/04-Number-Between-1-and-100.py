MIN_NUMBER = 1 # a constant, with capital letters always
MAX_NUMBER = 100 # a constant, with capital letters always
while True:
    number = float(input())
    if MIN_NUMBER <= number <= MAX_NUMBER:
        print (f'The number {number} is between {MIN_NUMBER} and {MAX_NUMBER}')
        break