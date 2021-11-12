def func(x):
    return x % 2 == 0


numbers_list = [1, 2, 3, 4, 5, 6]

# res = list(filter(lambda x: x % 2 == 0, numbers_list))
res = list(filter(func, numbers_list))  # returns the same as the code above
print(res)