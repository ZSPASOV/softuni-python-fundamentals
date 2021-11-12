numbers_string = input().split(' ')
numbers_string_sorted = sorted(numbers_string)
numbers_string_sorted.reverse()
string_for_print = ''

for string in numbers_string_sorted:
    string_for_print += string

print(string_for_print)
