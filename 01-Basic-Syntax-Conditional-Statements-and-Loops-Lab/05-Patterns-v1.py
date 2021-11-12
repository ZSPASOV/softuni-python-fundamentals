number = int(input())
for i in range(0, number + 1, 1):
    print('*' * i)
for j in range (number - 1, -1, -1):
    print('*' * j)