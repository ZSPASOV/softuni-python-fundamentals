# Formatting with the "%" operator

x = 'apples'
y = 'lemons'
z = "In the basket are %s and %s" % (x, y)
print(z)

# Formatting with the "{}" operators

x = 'apples'
y = 'lemons'
z = "In the basket are {} and {}".format(x, y)
print(z)

# Python 3 introduced new and simple way for string formatting called "f-String"

# Since Python 3 came out, it is the most used way for string formatting
x = 'apples'
y = 'lemons'
z = f"In the basket are {x} and {y}"
print(z)