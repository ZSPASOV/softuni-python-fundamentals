number_one = 3
number_two = 5
# for _ means empty variable
for _ in range(1, number_two + 1):
    number_one *= 2
    if number_one == 24:
        continue
    print(number_one)