def odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in number:
        if int(i) % 2 == 1:
            odd_sum += int(i)
        else:
            even_sum += int(i)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

n = input()
print(odd_and_even_sum(n))