def get_smallest_of_three_numbers(a, b, c):
    smallest = c

    if a < b and a < c:
        smallest = a
    elif b < a and b < c:
        smallest = b

    return smallest

first = int(input())
second = int(input())
third = int(input())

res = get_smallest_of_three_numbers(first, second, third)
print(res)