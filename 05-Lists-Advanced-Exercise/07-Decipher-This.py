sentence = input().split()
fixed_sentence = []
for i in sentence:
    word = i
    for_chr = ''
    for_letters = ''

    for j in range(len(word)):
        if word[j] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            for_chr += word[j]
            for_chr_letter = chr(int(for_chr))
        else:
            for_letters += word[j]

    for_letters_list = list(for_letters)
    for_letters_list[0] , for_letters_list[-1] = for_letters_list[-1] , for_letters_list[0]
    for_letters_final = ''.join(for_letters_list)
    fixed_sentence.append(for_chr_letter + for_letters_final)
    fix_for_print = ' '.join(fixed_sentence)
print(fix_for_print)




