# There are two ways you can loop through a list using for loops:

# iterating over the elements
my_list = ['dog', 'cat', 'fish']
for element in my_list:
    print(element, end=' ')

# using generated list with range
my_list2 = ['bear', 'fox', 'wolf']
for index in range(len(my_list2)):
    print(my_list2[index], end=' ')

# using enumerate - third optional way
my_list_3 = ['whale', 'beaver', 'mouse']
for i, v in enumerate(my_list_3):
    print(f'index = {i}, value = {v}')

