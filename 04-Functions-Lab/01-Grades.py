def receive_grade(value):
    if 2.00 <= value <= 2.99:
        return 'Fail'
    elif 3.00 <= value <= 3.49:
        return 'Poor'
    elif 3.50 <= value <= 4.49:
        return 'Good'
    elif 4.50 <= value <= 5.49:
        return 'Very Good'
    elif 5.50 <= value <= 6.00:
        return 'Excellent'

value = float(input())
print(receive_grade(value))