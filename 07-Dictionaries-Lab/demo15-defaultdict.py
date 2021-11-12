from collections import defaultdict

# defaultdict(int) creates an empty dictionary with default values 0
products = defaultdict(int)

products['asdf']
print(products['asdf'])
products['asdf'] += 1
print(products['asdf'])

d = defaultdict(lambda: 42)
d['a'] += 1
print(d['a'])