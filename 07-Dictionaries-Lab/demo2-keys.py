# While indexing is used with other container types to access values, dictionary uses keys
# Key can be used either inside square brackets or with the get() method
# The difference while using get() is that it returns None instead of KeyError, if the key is not found

my_dict = {'name': 'Jack', 'age': 26}
# Output: Jack
print(my_dict['name'])
# Output: 26
print(my_dict.get('age'))