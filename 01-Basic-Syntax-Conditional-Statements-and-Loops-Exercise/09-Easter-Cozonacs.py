budget = float(input())
price_1kg_flour = float(input())
number_cozonacs = 0
number_colored_eggs = 0
while budget > 0:
    price_per_cozonac = price_1kg_flour + 0.75 * price_1kg_flour + (price_1kg_flour * 1.25) / 4
    if price_per_cozonac > budget:
        break
    budget -= price_per_cozonac
    number_cozonacs += 1
    number_colored_eggs += 3
    if number_cozonacs % 3 == 0:
        number_colored_eggs -= number_cozonacs  - 2


print(f'You made {number_cozonacs} cozonacs! Now you have {number_colored_eggs} eggs and {budget:.2f}BGN left.')


