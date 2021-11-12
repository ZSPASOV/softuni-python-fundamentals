def loading_bar(number):
    loading_phase = '[' + (number // 10) * '%' + (10 - number // 10) * '.' +']'
    if number < 100:
        for_print = f'{number}% {loading_phase}\n Still loading...'
    elif number == 100:
        for_print = f'{number}% Complete!\n{loading_phase}'
    return for_print

number = int(input())

print(loading_bar(number))