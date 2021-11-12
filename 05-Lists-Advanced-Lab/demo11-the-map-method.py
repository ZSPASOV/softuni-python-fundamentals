# Using the map() method to convert list of strings to list of integers

strings_list = ["1", "2", "3", "4"]
numbers_list = list(map(lambda x: int(x), strings_list))
print(numbers_list)

# The map() method returns an iterator map object so you need to convert it into a list

# You will learn more about iterators and generators in the advanced python module


