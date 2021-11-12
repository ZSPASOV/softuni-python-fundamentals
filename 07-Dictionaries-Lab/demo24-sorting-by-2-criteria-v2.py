animals = {
    'tiger': 400,
    'bear': 600,
    'dog': 20,
    'animal': 20
}

animals_sorted = dict(sorted(animals.items(), key=lambda a: (-a[1], a[0])))

print(animals_sorted)