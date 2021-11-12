n_cars = int(input())
cars_garage = {}

for _ in range(n_cars):
    cars_stats = input().split('|')
    car = cars_stats[0]
    mileage = cars_stats[1]
    fuel = cars_stats[2]
    if car not in cars_garage:
        cars_garage[car] = []
    cars_garage[car] = [int(mileage), int(fuel)]

command = input()

while command != 'Stop':
    tokens = command.split(' : ')
    action = tokens[0]

    if action == 'Drive':
        car = tokens[1]
        distance = int(tokens[2])
        fuel = int(tokens[3])
        if cars_garage[car][1] < fuel:
            print('Not enough fuel to make that ride')
        else:
            #increasing mileage
            cars_garage[car][0] += distance
            #decreasing fuel
            cars_garage[car][1] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars_garage[car][0] >= 100000:
            cars_garage.pop(car)
            print(f'Time to sell the {car}!')
    if action == 'Refuel':
        car = tokens[1]
        fuel = int(tokens[2])
        if cars_garage[car][1] + fuel > 75:
            fuelled_with = 75 - cars_garage[car][1]
            cars_garage[car][1] = 75
            print(f'{car} refueled with {fuelled_with} liters')
        else:
            cars_garage[car][1] += fuel
            print(f'{car} refueled with {fuel} liters')

    if action == 'Revert':
        car = tokens[1]
        kilometers = int(tokens[2])
        if cars_garage[car][0] - kilometers < 10000:
            cars_garage[car][0] = 10000
        else:
            cars_garage[car][0] -= kilometers
            print(f'{car} mileage decreased by {kilometers} kilometers')

    command = input()

sorted_dict = dict(sorted(cars_garage.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in sorted_dict.items():
    print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')



