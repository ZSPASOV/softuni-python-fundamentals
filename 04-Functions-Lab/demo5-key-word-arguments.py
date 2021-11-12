# all default values parameters should be at the end

def say_hi(first_name, last_name):
    return f'Hello, {first_name} {last_name}'


# v1 - invoke with key word arguments
print(say_hi(last_name='Spasov', first_name='Zapryan'))
# v2 - invoke with positional arguments
print(say_hi('Zapryan', 'Spasov'))
# v3 - invoke with mix of positional arguments and key word arguments
# NOTE - key word arguments should be always AFTER the positional
print(say_hi('Zapryan', last_name='Spasov'))

# print(say_hi(first_name='Zapryan','Spasov'))
# will result to an error positional argument follows keyword argument
