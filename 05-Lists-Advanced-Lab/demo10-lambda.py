is_palindrome = lambda word: word == word[::-1]
print(type(is_palindrome))


# lambda funkciite trqbva da sa kratki
# dobre e da se sabirat na edin red
# lambda suzdava obekt koito moje da e izvikan kato funkciq
# v drugi ezici za programirane se narichat anonimni funkcii,
# zashtoto suzdavat funkcii bez ime

def sort_fn(item):
    return item[0]


sorted([1, 2, 3, 4], key=sort_fn)

# e edno i sushto sus:

sorted([1, 2, 3, 4], key=lambda item: item[0])

# lambda funkciite ne mogat da sudurzhat Statement:
# lambda item: a = 1  GRESHNO, zashtoto a = 1 e statement, a ne Expression
# lambda funkciite trqbva da vrushtat konkretna stoinost


