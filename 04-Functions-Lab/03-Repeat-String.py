def repeat_symbols(word, number_times):
    new_word = None
    new_word = word * number_times
    return new_word

word = input()
number_times = int(input())

print(repeat_symbols(word,number_times))