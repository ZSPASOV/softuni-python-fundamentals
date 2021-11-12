some_string = input()
my_list = some_string.split(' ')

empty_list = []
for i in range(len(my_list)):
    empty_list.append(-int(my_list[i]))
print(empty_list)
