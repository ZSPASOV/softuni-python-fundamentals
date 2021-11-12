# Check for Key Existence
# using the in keyword

# v1
my_dict = {'name': 'Peter', 'age': 22}
if 'name' in my_dict:
    print(my_dict['name'])

# v2
my_dict = {'name': 'Peter', 'age': 22}
if 'name' in my_dict.keys():
    print(my_dict['name'])