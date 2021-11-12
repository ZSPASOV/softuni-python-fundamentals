l = [1, 2, 2, 5, 2, 6, 2, 9, 2, 3, 3, 3, 3, 4, 2, 3]
# as a list of indexes
print([index for index, n in enumerate(l) if n == 2])
# as a tuple of index and value n
print([(index, n) for index, n in enumerate(l) if n == 2])

