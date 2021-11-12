# You can also use while loops to iterate through a list
# We use the pop function to remove the first element each iteration
# We iterate until the list is not empty
# v1

# pop(0) each time removes the first element of the list, with index 0
my_list = ["dog", "cat", "fish"]
while len(my_list) > 0:
    print(my_list[0], end=" ")
    my_list.pop(0)

# v2

# pop(0) each time removes the first element of the list, with index 0
print()  # to make the second loop on new line
my_list2 = ["wolf", "mouse", "fox"]
while len(my_list2) > 0:
    print(my_list2.pop(0), end=" ")

