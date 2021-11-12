number = int(input())
total_sum = 0

# note, the ord() function will return the ASCII numeric value mapping
# for each string
for i in range(1, number + 1):
    letter = input()
    total_sum += ord(letter)
print(f'The sum equals: {total_sum}')
