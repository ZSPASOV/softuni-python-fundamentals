def return_ascii_string(start, finish):

    empty_string = ''
    for i in range(ord(start) + 1, ord(end)):
        empty_string += chr(i) + ' '
    return empty_string


start = input()
end = input()

print(return_ascii_string(start, end))