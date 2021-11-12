input_string = input()

output_list = []

for i in range(len(input_string)):
    if input_string[i] == ':':
        print(f'{input_string[i]}{input_string[i+1]}')