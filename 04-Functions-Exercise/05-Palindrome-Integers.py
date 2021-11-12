def is_palindrome(text):
    counter = len(text) // 2
    palindrome_check = True

    for i in range(counter):
        second_index = len(text) - 1 - i
        if text[i] != text[second_index]:
            palindrome_check = False
            break
    return palindrome_check

def solve(items):

    for item in items:
        print(is_palindrome(item))

checked_input = input().split(', ')
solve(checked_input)
