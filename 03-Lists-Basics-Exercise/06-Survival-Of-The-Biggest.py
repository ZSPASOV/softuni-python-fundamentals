list_numbers = input().split(' ')
numbers_to_remove = int(input())
numeric_list = []
for i in list_numbers:
    numeric_list.append(int(i))

for i in range(numbers_to_remove):
    numeric_list.remove(min(numeric_list))

print(numeric_list)

