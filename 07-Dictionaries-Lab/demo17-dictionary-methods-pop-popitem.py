# pop() – removes the specific item from the dictionary

my_dict = {1: 'apple', 2: 'banana'}
apple = my_dict.pop(1)  # 'apple'
print(my_dict)  # {2: 'banana'}

# popitem() – removes the item that was last inserted
my_dict = {1: 'apple', 2: 'banana'}
print(my_dict.popitem())  # (2: 'banana')
print(my_dict)  # {1: 'apple'}