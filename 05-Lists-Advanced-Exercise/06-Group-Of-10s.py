input_list = input().split(', ')
input_num_list = list(map(int, input_list))
max_value = max(input_num_list)
if max_value % 10 == 0:
    number_of_groups = max_value // 10
else:
    number_of_groups = max_value // 10 + 1
lower_boundary = - 10
upper_boundary = 0

while len(input_num_list) > 0:
    for i in range(number_of_groups):
        lower_boundary += 10
        upper_boundary += 10
        list_to_print = [x for x in input_num_list if lower_boundary < x <= upper_boundary]
        input_num_list = [x for x in input_num_list if not(lower_boundary < x <= upper_boundary)]
        print(f"Group of {upper_boundary}'s: {list_to_print}")
