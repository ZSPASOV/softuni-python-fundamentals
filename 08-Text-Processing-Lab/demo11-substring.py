# You can use the replace() method to replace all occurrences of a
# specified phrase with another specified phrase

txt = "I like bananas bananas bananas bananas"
print(txt.replace("bananas", "apples"))  # I like apples

# If you only want to replace a certain number of phrases, add count

txt = "I like bananas bananas bananas"
x = txt.replace("bananas", "apples", 2)
print(x)

# If you only want to replace a certain number of phrases, add count
txt = "I like bananas bananas bananas"
x = txt.replace("bananas", "apples", -1)
print(x)
# - 1 is like the first example, replaces everywhere