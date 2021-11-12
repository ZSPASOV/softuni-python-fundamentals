start = int(input())
end = int(input())
result = ''

#note the chr function will return the character from ASCII table
#that is located on a certain position(an integer)

for i in range(start, end + 1):
    result += chr(i) + ' '

print(result)
