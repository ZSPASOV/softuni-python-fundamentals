import operator

operation = input()
a = int(input())
b = int(input())

def perform_operation(a, b, operation):
    operator_fn = None
    if operation == 'multiply':
        operator_fn = operator.mul
    elif operation == 'divide':
        operator_fn = operator.truediv
    elif operation == 'add':
        operator_fn = operator.add
    elif operation == 'subtract':
        operator_fn = operator.sub
    return int(operator_fn(a, b))


print(perform_operation(a, b, operation))
