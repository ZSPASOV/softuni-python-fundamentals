# The method items() returns a list of tuples where:
# keys are the first elements of each tuple
# values are the second elements of each tuple
# Sort descending by value first, then ascending by key:

my_dict = {'Peter': 18, 'George': 18, 'John': 45}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))
print(sorted_dict)
print(dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))))

# both print lines will return {'John': 45, 'George': 18, 'Peter': 18}