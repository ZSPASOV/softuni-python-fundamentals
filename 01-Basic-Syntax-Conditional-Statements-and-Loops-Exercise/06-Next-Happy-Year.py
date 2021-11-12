year = int(input())

while True:
    year += 1
    string_year = str(year)
    if len(string_year) == len(set(string_year)):
        break
print(year)






