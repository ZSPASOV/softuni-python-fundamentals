n = int(input())

plants = {}

for i in range(n):
    data = input().split('<->')
    plant = data[0]
    rarity = int(data[1])

    plants[plant] = {}
    plants[plant] = [rarity]


input_command = input()
while 'Exhibition' != input_command:
    tokens = input_command.split(': ')
    command = tokens[0]
    rest = tokens[1]
    if 'Rate' != command and 'Update' != command and 'Reset' != command:
        print('error')
    elif 'Rate' == command:
        plant_and_rating = rest.split(' - ')
        plant = plant_and_rating[0]
        rating = int(plant_and_rating[1])
        if plant not in plants:
            print('error')
        else:
            plants[plant].append(rating)

    elif 'Update' == command:
        plant_and_new_rarity = rest.split(' - ')
        plant = plant_and_new_rarity[0]
        new_rarity = int(plant_and_new_rarity[1])
        if plant not in plants:
            print('error')
        else:
            plants[plant][0] = new_rarity

    elif 'Reset' == command:
        plant = rest
        if plant not in plants:
            print('error')
        else:
            plants[plant] = [plants[plant][0]]



    input_command = input()


print('Plants for the exhibition:')

for key, value in plants.items():
    if len(value) > 1:
        average = sum(value[1:]) / (len(value) - 1)
    else:
        average = 0.00
    plants[key].append(average)



sorted_dict = dict(sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][-1])))


for key, value in sorted_dict.items():
    print(f'- {key}; Rarity: {value[0]}; Rating: {value[-1]:.2f}')





