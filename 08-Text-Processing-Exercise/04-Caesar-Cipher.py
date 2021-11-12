input_string = input()
output_string = ''
for i in input_string:
    output_string += chr(ord(i) + 3)
print(output_string)
