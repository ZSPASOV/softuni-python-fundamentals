list_money = input().split(', ')
list_money_num = []
number_of_beggars = int(input())
sum_money_per_beggar = []

for i in list_money:
    list_money_num.append(int(i))

for i in range(number_of_beggars):
    sum_money_per_beggar.append(0)

index = 0

for i in list_money_num:
    sum_money_per_beggar[index] += i
    index += 1

    if index == number_of_beggars:
        index = 0

print(sum_money_per_beggar)



