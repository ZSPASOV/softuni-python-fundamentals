# Python offers many ways to substring a string
# It is often called "slicing"
# Slicing can also be used with lists
# It is equivalent to the slice() method

text = "My name is Peter"
name = text[-5:]
print(name)

# same as text[11:] or text[slice(-5, 16, 1)]
print(text[slice(-5, 16, 1)])