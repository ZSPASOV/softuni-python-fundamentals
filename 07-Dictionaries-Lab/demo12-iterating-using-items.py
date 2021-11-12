# Iterating Using Items()

# It returns tuple (key, value) pairs
# Using the items() method to iterate through key-value pairs

squares = {1: 1, 2: 4, 3: 9}
for (key, value) in squares.items():
    print(f"Key: {key}, Value: {value}")