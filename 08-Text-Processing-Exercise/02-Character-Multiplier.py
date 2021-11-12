names = input().split()
str1 = names[0]
str2 = names[1]
output_num = 0
shorter_range = min(len(str1), len(str2))
longer_range = max(len(str1), len(str2))
longer_string = ''
if len(str1) > len(str2):
    longer_string = str1
elif len(str2) > len(str1):
    longer_string = str2

for i in range(shorter_range):
    output_num += ord(str1[i]) * ord(str2[i])

if len(str1) != len(str2):
    for i in range(shorter_range, longer_range):
        output_num += ord(longer_string[i])


print(output_num)