stock_products = input().split(' ')
search_products = input().split(' ')

stock_dict = {}

for i in range(0, len(stock_products), 2):
    key = stock_products[i]
    value = stock_products[i + 1]
    stock_dict[key] = int(value)

for i in search_products:
    if i in stock_dict:
        print(f'We have {stock_dict[i]} of {i} left')
    else:
        print(f'Sorry, we don\'t have {i}')