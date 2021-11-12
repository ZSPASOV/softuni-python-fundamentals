divisor = int(input())
bound = int(input())
n = 0

while True:
    n += 1
    if n % divisor == 0 and (n + divisor) > bound:
        break

print(n)



