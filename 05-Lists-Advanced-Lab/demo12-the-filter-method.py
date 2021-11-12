# Using the filter() method to filter elements that fulfill a given condition

numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter((lambda x: x % 2 == 0), numbers_list))
print(even_numbers)

# The filter() method also returns an iterator object so you have to again convert it into a list

print(list(map(lambda n: n + 2, [1, 2, 3, 4, 5, 6])))


# this is the same as:

def add_two(n):
    return n + 2


print(list(map(add_two, [1, 2, 3, 4, 5, 6])))

# using lambda as a parameter of the function map is more elegant


