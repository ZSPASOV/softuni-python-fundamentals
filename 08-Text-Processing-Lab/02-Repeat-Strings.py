list_a = input().split(' ')
empty_str = ''
for i in list_a:
    empty_str += len(i) * i
print(empty_str)