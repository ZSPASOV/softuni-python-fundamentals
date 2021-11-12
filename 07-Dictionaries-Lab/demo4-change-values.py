# Dictionaries are mutable
# We can add new items or change the value of existing items using assignment operator
# If the key is already present, value gets updated, else a new pair is added to the dictionary

my_dict = {'name': 'Jack', 'age': 26}
my_dict['age'] = 27  # update
print(my_dict['age'])  # 27