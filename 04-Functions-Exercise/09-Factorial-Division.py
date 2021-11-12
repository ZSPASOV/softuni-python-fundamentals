def factorial_division(first_num, second_num):
    factorial_one = 1
    factorial_two = 1
    for i in range(first_num, 0, -1):
        factorial_one *= i
    for i in range(second_num, 0, -1):
        factorial_two *= i
    result = factorial_one / factorial_two
    return (f'{result:.2f}')

first_num = int(input())
second_num = int(input())

print(factorial_division(first_num, second_num))