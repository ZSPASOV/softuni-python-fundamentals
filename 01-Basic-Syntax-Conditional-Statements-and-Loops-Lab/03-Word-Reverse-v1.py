word = input()
reversed_word = ''
#first argument of range is len(word)-1, it takes the number of symbols in the string - 1, because it starts from 0
#second argument in range is -1, so the loop will continue to -1, since the second is excluding it will stop at 0 - the first symbol of the string
#third argument in range is -1, the step, that it loops backwards
for index in range(len(word)-1, - 1, - 1):
    reversed_word += word[index]
print(reversed_word)