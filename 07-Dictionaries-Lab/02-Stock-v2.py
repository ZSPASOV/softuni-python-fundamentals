stock_products = input().split(' ')

stock_dict = {}

for i in range(0, len(stock_products), 2):
    stock_dict[stock_products[i]] = int(stock_products[i + 1])

search_products = input().split(' ')
for i in search_products:
    quantity = stock_dict.get(i)
    if quantity:
        print(f'We have {quantity} of {i} left')
    else:
        print(f'Sorry, we don\'t have {i}')