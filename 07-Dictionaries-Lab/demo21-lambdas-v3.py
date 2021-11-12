# It can take multiple parameters

x = lambda a, b: a * b
print(x(3, 4))  # 12

full_name = lambda first, last: f'I am {first} {last}'
result = full_name('Guido', 'van Rossum')
print(result)  # I am Guido van Rossum

# With the sort() method you pass the lambda function as key

my_dict = {'Peter': 21, 'George': 18, 'John': 45}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict)