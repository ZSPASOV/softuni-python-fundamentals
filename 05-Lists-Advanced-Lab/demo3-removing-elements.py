# using the clear() method - removes all elements
my_list = [1, 2, 3]
my_list.clear()
print(my_list)

# using the pop() method - removes the last element and returns it
my_list_two = [1, 2, 3]
last = my_list_two.pop()
print(my_list_two)
print(last)
# removes by value (first occurrence)

my_list_three = [1, 2, 3]
my_list_three.remove(1)
print(my_list_three)