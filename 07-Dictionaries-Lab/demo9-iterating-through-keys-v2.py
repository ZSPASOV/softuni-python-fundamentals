# Changing the values by iterating through the keys

squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    squares[key] *= 2
print(squares)
# {1: 2, 2: 8, 3: 18}