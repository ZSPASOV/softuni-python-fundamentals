quantity = int(input())
days_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

days_count = 1
christmas_spirit = 0
total_cost = 0

while days_count <= days_until_christmas:

    if days_count % 11 == 0:
        quantity += 2

    if days_count % 2 == 0:
        christmas_spirit += 5
        total_cost += ornament_set_price * quantity

    if days_count % 3 == 0:
        christmas_spirit += 13
        total_cost += tree_skirt_price * quantity + tree_garlands_price * quantity

    if days_count % 5 == 0:
        christmas_spirit += 17
        total_cost += tree_lights_price * quantity
        if days_count % 3 == 0:
            christmas_spirit += 30

    if days_count % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_skirt_price + tree_garlands_price + tree_lights_price

    days_count += 1

if days_until_christmas % 10 == 0:
    christmas_spirit -= 30


print(f'Total cost: {total_cost}\nTotal spirit: {christmas_spirit}')
