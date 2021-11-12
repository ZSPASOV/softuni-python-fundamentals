capacity = 255
n = int(input())
total_liters = 0

for _ in range (n):
    poured_amount = int(input())
    if total_liters +  poured_amount > capacity:
        print('Insufficient capacity!')
    else:
        total_liters += poured_amount
print(total_liters)
