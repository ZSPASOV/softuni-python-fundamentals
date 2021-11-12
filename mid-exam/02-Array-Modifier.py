input_num_list = list(map(int, input().split()))
input_command = input()
args = None
command = None
first_args = None
second_args = None

while input_command != 'end':
    if input_command == 'decrease':
        input_num_list = list(map(lambda n: n - 1, input_num_list))

    else:
        args = input_command.split(' ')

        command = args[0]
        first_args = int(args[1])
        second_args = int(args[2])

        if command == 'swap':
            input_num_list[first_args], input_num_list[second_args] = input_num_list[second_args], input_num_list[first_args]

        if command == 'multiply':
            product = input_num_list[first_args] * input_num_list[second_args]
            input_num_list[first_args] = product

    input_command = input()



    if input_command == 'end':
        break

input_num_list_str = list(map(str, input_num_list))
print(', '.join(input_num_list_str))