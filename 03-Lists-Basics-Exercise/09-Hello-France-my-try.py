list_of_items = input().split('|')
budget = float(input())
new_prices = []
new_prices_string = []
invested = 0
for item in list_of_items:
    type = item.split('->')
    if type[0] == 'Clothes' and float(type[1]) > 50.00:
        continue
    elif type[0] == 'Shoes' and float(type[1]) > 35.00:
        continue
    elif type[0] == 'Accessories' and float(type[1]) > 20.50:
        continue
    elif budget >= float(type[1]):

        budget -= float(type[1])
        invested += float(type[1])
        a = (float(type[1]) * 1.4)
        b = round(a,2)
        new_prices.append(b)

profit = sum(new_prices) - invested

for new_price in new_prices:
    print(f'{new_price:.2f}', end = ' ')
print(' ')
print(f'Profit: {profit:.2f}')
if budget + sum(new_prices) > 150:
    print('Hello, France!')
else:
    print('Time to go.')


