my_dict = {'Peter': 21, 'George': 18, 'John': 45, 'Yuri': 45}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict)

# EXPLAINED:

# sorted ot rechnik bi vurnalo samo list s keys. zatova izpolzvame .items()
# s .items() sorted shte vurne tuples - key plus value
# za da oburnem tuples-a v rechnik otnovo slagame dict() okolo vsichko
# key = lambda x: x[1] - tova znachi da sortira po stoinost.
# v sluchaq x e tuple koito podavame na lambda funkciqta
# x[1] e vtoriqt element ot vseki tuple, toest value (stoinostta)
# taka shte sortira po vuzrast rechnika

# v2 - ako iskame da sortira po nizhodqsht red slagame - x[1].
# tova bi rabotilo samo pri chisla stoinosti
my_dict = {'Peter': 21, 'George': 18, 'John': 45, 'Yuri': 45}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: -x[1]))
print(sorted_dict)

# tova e sushtoto kato reversed = true i bez minus pred x[1]
my_dict = {'Peter': 21, 'George': 18, 'John': 45, 'Yuri': 45}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)

# ako iskame da sortirame po stoinost, vzimame purvi index na tuple, x[0]
my_dict = {'Peter': 21, 'George': 18, 'John': 45, 'Yuri': 45}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
print(sorted_dict)

# ako iskame obratno po string , koeto e v sluchaq purvi index na tuple, koeto e key
# polzvame reverse=True
my_dict = {'Peter': 21, 'George': 18, 'John': 45, 'Yuri': 45}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0], reverse=True))
print(sorted_dict)

# sortirane purvo po stoinost, posle po key - Yuri i John sa na 45, no John e predi Yuri po azbuka
my_dict = {'Peter': 21, 'George': 18, 'John': 45, 'Yuri': 45}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (x[1], x[0])))
print(sorted_dict)

# sortirane purvo po key posle po stoinost
my_dict = {'Peter': 21, 'George': 18, 'John': 45, 'Yuri': 45}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (x[0], x[1])))
print(sorted_dict)

