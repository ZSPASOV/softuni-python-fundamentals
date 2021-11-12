string_a = input()
string_b = input()

for i in range (len(string_a)):
    if string_a[i] != string_b[i]:
        for string_b_index in range(0, i + 1):
            print(string_b[string_b_index], end='')

        for string_a_index in range (i + 1, len(string_a)):
            print(string_a[string_a_index], end='')

        print()


