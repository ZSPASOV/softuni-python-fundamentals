words = input().split(', ')
text = input()
list_c = []


for word in words:
    if word in text:
        list_c.append(word)

print(list_c)