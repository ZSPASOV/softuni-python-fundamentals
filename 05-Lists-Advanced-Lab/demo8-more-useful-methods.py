# Using the count() method  Finds all occurrences in a list
my_list = [1, 2, 3, 2, 2]
print(my_list.count(2))

# Using the index() method Finds the index of the first occurrence
my_list = [1, 2, 3, 2, 2]
last = my_list.index(2)
print(last)

# Using the reverse() method Reverses the elements

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)

# note .reverse() MUTATES directly the element on which it is applied

my_tuple = (1, 2, 3).reverse()