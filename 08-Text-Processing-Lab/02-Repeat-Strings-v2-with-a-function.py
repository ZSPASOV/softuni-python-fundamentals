def repeat_by_length(word):
    return word * len(word)

words = input().split(' ')
print(''.join(map(repeat_by_length, words)))