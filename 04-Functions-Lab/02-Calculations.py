def perform_operation(operation, a, b):
    result = None
    if operation == 'multiply':
        result = int(a * b)
    elif operation == 'divide':
        result = int(a / b)
    elif operation == 'add':
        result = int(a + b)
    elif operation == 'subtract':
        result = int(a - b)
    return result

operation = input()
a = int(input())
b = int(input())

print(perform_operation(operation, a, b))
