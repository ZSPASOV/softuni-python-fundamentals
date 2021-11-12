command = input()
product_data = {}

while command != 'buy':
    args = command.split(' ')
    product = args[0]
    price = float(args[1])
    quantity = int(args[2])
    if product not in product_data:
        product_data[product] = [0, 0]
    product_data[product][0] = price
    product_data[product][1] += quantity

    command = input()

for key, value in product_data.items():
    print(f'{key} -> {value[0] * value[1]:.2f}')

