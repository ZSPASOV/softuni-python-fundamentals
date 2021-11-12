words = input().split(', ')
text = input()
list_c = []

list_c = [word for word in words if word in text]

print(list_c)