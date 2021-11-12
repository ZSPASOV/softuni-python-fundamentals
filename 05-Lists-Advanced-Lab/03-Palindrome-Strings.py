def is_palindrome(word):
    return word == word[::-1] # option 1
    # return word == ''.join(reversed(word)) # option 2

words = input().split(' ')
searched_palindrome = input()

# creating a list with list comprehension
palindromes = [word for word in words if is_palindrome(word)]

print(palindromes)
print(f'Found palindrome {palindromes.count(searched_palindrome)} times')