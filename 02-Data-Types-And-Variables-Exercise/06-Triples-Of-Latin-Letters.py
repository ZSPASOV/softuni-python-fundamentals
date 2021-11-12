n = int(input())

#small latin letters in ASCII table start from 97 (97 = a, 98 = b, 99 = c, 100 = d, etc)
for first in range(n):
    for second in range(n):
        for third in range(n):
            print(f'{chr(first + 97)}{chr(second + 97)}{chr(third + 97)}')

