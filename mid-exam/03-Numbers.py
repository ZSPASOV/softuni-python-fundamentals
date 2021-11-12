input_num_list = list(map(int, input().split()))
more_than_average = []
top_five = []
average = sum(input_num_list) / len(input_num_list)

for i in input_num_list:
    if i > average:
        more_than_average.append(i)


for i in range(5):
    if len(more_than_average) == 0:
        break
    max_num = max(more_than_average)
    more_than_average.remove(max_num)
    top_five.append(max_num)




top_five_str = list(map(str, top_five))
if len(top_five) == 0:
    print('No')
else:
    print(' '.join(top_five_str))