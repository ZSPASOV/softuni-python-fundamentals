def parse_num(string):
    return int(string)


string_list = ['1', '2', '3', '4']

res_1 = list(map(lambda n: int(n), string_list))
res_2 = list(map(int, string_list))
res_3 = list(map(parse_num, string_list))

# res_1 res_2 and res_3 are the same, the code above does the same thing
# in different ways
# note in map when you put a function as a first parameter you do not give () after function`s name
print(res_1)
print(res_2)
print(res_3)